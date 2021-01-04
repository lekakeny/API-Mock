from rest_framework import routers

from .views import  CustomerViewSet

router = routers.DefaultRouter()
router.register(r'mock', CustomerViewSet, 'mock')

urlpatterns = router.urls