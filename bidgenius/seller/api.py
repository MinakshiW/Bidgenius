from rest_framework import generics
from seller.serializers import ProductInfoSerializer,ProductCategorySerializer,ProductImageSerializer,ProductImagesSerializer, ProductSerializer
from accounts.serializers import UserSerializer
from seller.models import ProductInformation,ProductCategory,ProductImages
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

class ProductInfoCreateView(generics.CreateAPIView,generics.ListAPIView):
    serializer_class = ProductInfoSerializer
    queryset = ProductInformation.objects.all()
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return super().get_serializer_class()

    # def get_queryset(self):
    #     user = self.request.user
    #     return ProductInformation.objects.filter(owner=user)
class ProductRetrieveView(generics.RetrieveAPIView):
    serializer_class = ProductInfoSerializer
    queryset = ProductInformation.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return super().get_serializer_class()


class ProductCategoryListView(generics.ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class ProductImageCreateView(generics.CreateAPIView,generics.ListAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImages.objects.all()
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product']



class ProductimagesAPI(viewsets.ModelViewSet):
    serializer_class = ProductImagesSerializer
    queryset = ProductImages.objects.all()
    http_method_names = ['get']
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
   

    
