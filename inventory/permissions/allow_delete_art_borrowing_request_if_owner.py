from rest_framework.permissions import DjangoModelPermissions

class AllowDeleteArtBorrowingRequestIfOwner(DjangoModelPermissions):
    """
    Object-level permission to only allow owners of an art borrowing request.
    Assumes the model instance has an `requester` attribute.
    """

    def has_object_permission(self, request, view, obj):
        is_municipality_worker = bool(
            request.user.groups.filter(name='municipality_workers'))
        if is_municipality_worker and request.method == 'DELETE' and obj.requester != request.user:
            return False
        return self.has_permission(request, view)
