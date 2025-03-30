from django.urls import include, path
from rest_framework import routers

from api.v1.views import WalletViewSet

app_name = 'news'

router_v1 = routers.DefaultRouter()
router_v1.register('wallets', WalletViewSet, basename='wallets')

urlpatterns = [
    path('', include(router_v1.urls)),
]
