from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):         #allow user edit own profile
    def has_object_permission(self, request, view, obj):    #Check if user is trying to edit his own pprofile
        if request.metho in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id    
