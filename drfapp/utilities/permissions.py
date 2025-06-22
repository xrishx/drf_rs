from rest_framework.permissions import BasePermission

SUPER_ADMIN = 1
ADMIN = 2

# Important 
def IsAuthenticated(request): 
    return bool(request.user and request.user.is_authenticated)

def SuperAdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.is_superuser)

def AdminLevel(request):
    return bool(IsAuthenticated(request) and request.user.role in [ADMIN])

def IsOwner(request):
    if str(request.user.id) == str(request.data.get('user')):
        return True
    elif len(request.data) == 0 and len(request.POST) == 0:
        return True
    return False

class BookPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        if view.action in ['retrieve']:
            return True
        if view.action in ['create', 'update', 'partial_update']:
            return SuperAdminLevel(request) or AdminLevel(request) or IsOwner(request)
        if view.action in ['destroy']:
            return IsOwner(request)
            