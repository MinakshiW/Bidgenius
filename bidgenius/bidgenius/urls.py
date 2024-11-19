
from django.contrib import admin

from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from rest_framework.routers import DefaultRouter
from seller.api import AdminProductInformationAPI, AdminProductimagesAPI
from auctions.api import AuctionDetailsAPI


from accounts.api import UserModelViewSet
from seller.api import ProductimagesAPI

router = DefaultRouter()
router.register('adminproducts', AdminProductInformationAPI, basename='adminproduct')
router.register('adminproductsimages', AdminProductimagesAPI, basename='adminproductsimages')
router.register('auctionDetails', AuctionDetailsAPI, basename='auctionDetails')

router.register('users',UserModelViewSet,basename="users")
router.register('productimages',ProductimagesAPI,basename="productimages")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('seller.urls')),
    path('',include('auctions.urls')),
    path('',include(router.urls)),
    path('access/',token_obtain_pair),
    path('refresh/',token_refresh),

    path('', include('accounts.urls')),

  

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
