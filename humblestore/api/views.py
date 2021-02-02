from rest_framework import viewsets
from rest_framework import permissions
from humblestore.api.serializers import HumbleBundleSerializer, HumbleItemSerializer
from humblestore.models import HumbleBundle, HumbleItem


class HumbleBundleViewSet(viewsets.ModelViewSet):
    """API endpoint to view or edit the Humble Bundle"""

    queryset = HumbleBundle.objects.all().order_by("-bundle_name")
    serializer_class = HumbleBundleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HumbleItemViewSet(viewsets.ModelViewSet):
    """API endpoint to view or edit the Humble Item"""

    queryset = HumbleItem.objects.all().order_by("id")
    serializer_class = HumbleItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
