from rest_framework.permissions import DjangoModelPermissions

class AllowDeleteArtBorrowingRequestIfOwner(DjangoModelPermissions):
    """
    Object-level permission to only allow owners of an art borrowing request.
    Assumes the model instance has an `requester` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return obj.requester == request.user and request.method == 'DELETE' \
            or self.has_permission(request, view)
