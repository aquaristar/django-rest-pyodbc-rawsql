from django.conf.urls import url, include
from rest_framework import routers
from abcapi import views

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pyapi/users', views.UserViewSet)
router.register(r'pyapi/groups', views.GroupViewSet)

router.register(r'pyapi/order', views.OrderViewSet)
router.register(r'pyapi/gift', views.DskGiftMainViewSet)
router.register(r'pyapi/inventory', views.Da7InventoryStoreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
	url(r'^', include(router.urls)),
#    url(r'pyapi/gift', views.DskGiftMainViewSet),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]