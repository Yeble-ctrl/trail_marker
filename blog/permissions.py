from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object
        # Traverse relationships to check ownership
        if hasattr(obj, 'owner'):  # Direct ownership (e.g., Blog)
            return obj.owner == request.user
        elif hasattr(obj, 'blog'):  # Indirect ownership via BlogPost
            return obj.blog.owner == request.user
        elif hasattr(obj, 'blogPost'):  # Indirect ownership via BlogPostPhoto
            return obj.blogPost.blog.owner == request.user

        return False