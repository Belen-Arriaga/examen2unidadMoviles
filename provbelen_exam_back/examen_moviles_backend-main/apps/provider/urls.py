from rest_framework import routers

from apps.provider.views import ProviderViewSet

router = routers.DefaultRouter()
router.register('providers', ProviderViewSet, basename='providers')
router.register('suppliers', ProviderViewSet, basename='suppliers')

urlpatterns = router.urls
