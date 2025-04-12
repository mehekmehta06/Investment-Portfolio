from rest_framework.response import Response
from rest_framework.views import Response
from portfolioapp.permissions import IsMemberPermission
from .forms import *
import decimal
from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes, permission_classes, action
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import * 
import requests
import razorpay
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .permissions import IsMemberPermission

#Register-Login-Logout
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if username and '@' in username:
            try:
                user = UserProfile.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#user get-post-put-delete
class UserProfileDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def put(self, request, pk):
        try:
            user = UserProfile.objects.get(pk=pk)
            serializer = UserProfileSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, username):
        try:
            user = UserProfile.objects.get(username=username)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except UserProfile.DoesNotExist:
            raise Http404('User not found')    
class UserProfileAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        try:
            user = UserProfile.objects.all()
            serializer = UserProfileSerializer(user,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#portfolio get-post-delete-put
class PortfolioAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsMemberPermission]

    def get(self,request,pk):
        try:
            queryset = PortfolioModel.objects.get(pk=pk)
            serializer = PortfolioModelSerializer(queryset,partial=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"Object not found"},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
            serializer = PortfolioModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = PortfolioModel.objects.get(pk=pk)
            serializer = PortfolioModelSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            user = PortfolioModel.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'portfolio deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except UserProfile.DoesNotExist:
            raise Http404('Portfolio not found')
       
        
#current get
class CurrentMarketAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    

    def get_api_data(self):
        url = 'https://financialmodelingprep.com/api/v3/stock/list?apikey=jO0rmvl301In61hIIj6gbpHeftAwI0Fn'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as e:
            print(f"error fetching api data: {e}")
            return []
    
    def get(self, request, *args, **kwargs):
        queryset = CurrentMarketModel.objects.all()
        serializer = CurrentMarketModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        api_data = self.get_api_data()
        if not api_data:
            return Response(
                {"detail": "Unable to fetch data from the api"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        for entry in api_data:
            print(type(entry))
            if isinstance(entry, list):
                for item in entry:
                    if isinstance(item, dict):
                        symbol = item.get('symbol', '')
                        name = item.get('name', '')
                        price = item.get('price', 0.0)
                        exchange = item.get('exchange', '')
                        entry_type = item.get('type', '')
                        print(type(price))
                        try:
                            CurrentMarketModel.objects.create(
                                    symbol=symbol,
                                    stockname=name,
                                    stockamt=price,
                                    exchange=exchange,
                                    type=entry_type
                                )
                             
                        except Exception as e:
                            #print(f"error fetching api data: {e}")
                            break
                    else:
                        print(f"Unexpected item type within list: {type(item)}")                   
            elif isinstance(entry, dict):
                
                symbol = entry.get('symbol', '')
                name = entry.get('name', '')
                price = entry.get('price', 0.0)
                exchange = entry.get('exchange', '')
                entry_type = entry.get('type', '')
                print(type(price))
                try:
                    CurrentMarketModel.objects.create(
                        symbol=symbol,
                        stockname=name,
                        stockamt=price,
                        exchange=exchange,
                        type=entry_type
                    )
                except Exception as e:
                    pass
                    #print(f"error fetching api data: {e}")
            else:
                print(f"Unexpected entry type: {type(entry)}")
        return Response(
            {"detail": f"Data from API successfully saved to the database. {len(api_data)} entries added."},
            status=status.HTTP_201_CREATED
        )

#investment get-put-delete        
class InvestmentAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        try:
            queryset = InvestmentModel.objects.get(pk=pk)
            serializer = InvestmentModelSerializer(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"Object not found"},status=status.HTTP_404_NOT_FOUND)

    def post(self, request, Fname):
        try:
            portfolio_data = PortfolioModel.objects.get(Fname=Fname)
            user_data=UserProfile.objects.get(Fname=Fname)
        except PortfolioModel.DoesNotExist:
            return Response({'error': 'Portfolio data not found for the given user.'}, status=status.HTTP_400_BAD_REQUEST)
        stock_price = portfolio_data.stock_price
        stock_number = portfolio_data.stock_number
        mf_amt = portfolio_data.mf_amt
        roi =stock_price * stock_number 
        valuation = int(roi * mf_amt)
        email = user_data.pk
        investment_data = {
            'roi': roi,
            'email': email,
            'valuation': valuation,
        }
        serializer = InvestmentModelSerializer(data=investment_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#resorce get-post          
class ResourceAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = ResourcesModel.objects.all()
        serializer = ResourcesModelSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_api_data(self):
            url= 'https://financialmodelingprep.com/api/v3/fmp/articles?page=0&size=5&apikey=jO0rmvl301In61hIIj6gbpHeftAwI0Fn'        
            try:
                response = requests.get(url)
                print(type(response))
                response.raise_for_status()
                data = response.json()
                #print(data)
                return data["content"]
            except requests.RequestException as e:
                print(f"error fetching api data: {e}")
            return []
    def post(self, request):
        api_data = self.get_api_data()
        #dict(api_data)
        print(type(api_data))
        print(api_data)
        if not api_data:
            return Response(
                {"detail": "Unable to fetch data from the api"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )     
        #data=api_data["content"]
        for entry in api_data:
            #print(entry)
            if isinstance(entry, list):
                for item in entry:
                    if isinstance(item, dict):
                        title = item.get('title', '')
                        author=item.get('author','')
                        link=item.get('link','')
                        try:
                            ResourcesModel.objects.create(
                                    books=title,
                                    author=author,
                                    link=link
                                )
                        except Exception as e:
                            print(f"error fetching api data: {e}")
                    else:
                        print(f"Unexpected item type within list: {type(item)}")                   
            elif isinstance(entry, dict):
                title = entry.get('title', '')
                author=entry.get('author','')
                link=entry.get('link','')
                try:
                    ResourcesModel.objects.create(
                        books=title,
                        author=author,
                        link=link
                    )
                except Exception as e:
                    print(f"error fetching api data: {e}")
            else:
                print(f"Unexpected entry type: {type(entry)}")
        return Response(
            {"detail": f"Data from API successfully saved to the database. {len(api_data)} entries added."},
            status=status.HTTP_201_CREATED
        )    
    
def payment(request,username):
    
        amount= 50000
        order_currency='INR'
        user_profile = get_object_or_404(UserProfile, username=username)
        client= razorpay.Client(
            auth=('rzp_test_FAXa7yjtACuDCu','MCKxZpfzL2iQA0KAZqnhVhDy'))
        
        request_payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(request_payment)

        order_id=request_payment['id']
        order_status=request_payment['status']
        order_created=request_payment['created_at']
        
        if order_status == 'created':
            
            TransactionlogModel.objects.create(
                            amount=500,
                            trans_id=order_id,
                            email=user_profile,
                            razorpay_id=order_created,
                            paid=True
                        )
              

        return render(request,'mem_payment.html',{'request_payment':request_payment,'some_value':username})

@csrf_exempt
def success(request,username):
    user_profile = get_object_or_404(UserProfile, username=username)
    MembershipModel.objects.create(
        time_period=30,
        email=user_profile,
        
    )
    
    return HttpResponse("Your Payment Was Successful") 
                                                                   
    
    #custom command in django
    #current model single stocknsme ka info
    #token se permission
    #swagger docs
    
    
    