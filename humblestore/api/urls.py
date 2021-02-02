from rest_framework.routers import DefaultRouter
from humblestore.api import views

router = DefaultRouter()

router.register(r"humblebundle", views.HumbleBundleViewSet)
router.register(r"humbleitem", views.HumbleItemViewSet)
