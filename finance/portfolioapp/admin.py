from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

#UserProfile = get_user_model()
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('Fname','Lname','username','email')
admin.site.register(UserProfile,UserProfileAdmin)

class PortfolioModelAdmin(admin.ModelAdmin):
    list_display=('Fname','Lname','contact_no','email','stock_name','stock_number','stock_price','stock_date','mf_name','mf_amt','mf_date')
admin.site.register(PortfolioModel,PortfolioModelAdmin)

class CurrentMarketModelAdmin(admin.ModelAdmin):
    list_display=('stockname','stockamt','symbol','type','exchange')
admin.site.register(CurrentMarketModel,CurrentMarketModelAdmin)

class InvestmentModelAdmin(admin.ModelAdmin):
    list_display=('roi','valuation','email')
admin.site.register(InvestmentModel,InvestmentModelAdmin)

class ResourcesModelAdmin(admin.ModelAdmin):
    list_display=('books','author','link')
admin.site.register(ResourcesModel,ResourcesModelAdmin)

class MembershipModelAdmin(admin.ModelAdmin):
    list_display=('mem_id','start_time','email','time_period')
admin.site.register(MembershipModel,MembershipModelAdmin)

class TransactionlogModelAdmin(admin.ModelAdmin):
    list_display=('amount','razorpay_id','paid','trans_id','email')
admin.site.register(TransactionlogModel,TransactionlogModelAdmin)


