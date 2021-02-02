from rest_framework.routers import DefaultRouter
from core.api import views

router = DefaultRouter()

router.register(r"application", views.ApplicationViewSet)
router.register(r"developer", views.DeveloperViewSet)
router.register(r"person", views.PersonViewSet)
router.register(r"platform", views.PlatformViewSet)
router.register(r"publisher", views.PublisherViewSet)
