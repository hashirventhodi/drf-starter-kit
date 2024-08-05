from functools import wraps
from rest_framework.exceptions import PermissionDenied

def has_permission(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.has_perm(permission):
                raise PermissionDenied("You do not have permission to perform this action")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator