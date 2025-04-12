
from rest_framework import permissions
from .models import UserProfile, MembershipModel

class IsMemberPermission(permissions.BasePermission):
    def has_permission(self, request, view,**kwargs):
        pk = view.kwargs.get('pk')  
        user_profile = UserProfile.objects.get(pk=pk)
        user=user_profile.email
        membership_exists = MembershipModel.objects.filter(email=user).exists()
        print(f"User Profile: {user_profile}")
        print(f"Membership Exists: {membership_exists}")
        return membership_exists
