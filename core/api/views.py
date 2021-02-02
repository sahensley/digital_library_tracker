from rest_framework import permissions
from rest_framework import viewsets

from core.api.serializers import (
    ApplicationSerializer,
    DeveloperSerializer,
    PersonSerializer,
    PlatformSerializer,
    PublisherSerializer,
)
from core.models import Application, Developer, Person, Platform, Publisher


class ApplicationViewSet(viewsets.ModelViewSet):
    """API endpoint to view or edit the Applications"""

    queryset = Application.objects.all().order_by("application_name")
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DeveloperViewSet(viewsets.ModelViewSet):
    """API endpoint to view or edit the Developers"""

    queryset = Developer.objects.all().order_by("developer")
    serializer_class = DeveloperSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PersonViewSet(viewsets.ModelViewSet):
    """API endpoint to view or edit the Persons"""

    queryset = Person.objects.all().order_by("person_name")
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlatformViewSet(viewsets.ModelViewSet):
    """API endpoint to view or edit the Platforms"""

    queryset = Platform.objects.all().order_by("platform")
    serializer_class = PlatformSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PublisherViewSet(viewsets.ModelViewSet):
    """API endpoint to view or edit the Publishers"""

    queryset = Publisher.objects.all().order_by("publisher")
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
