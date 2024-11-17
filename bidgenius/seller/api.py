from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import ProductInformationSerializer, ProductImagesSerializer
from .models import ProductInformation, ProductImages
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

class AdminProductInformationAPI(viewsets.ModelViewSet):
    serializer_class = ProductInformationSerializer
    queryset = ProductInformation.objects.all()
    http_method_names = ['get', 'patch']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def filter_products(self, request):
        q = request.query_params.get('q', None)
        queryset = self.queryset
        print(q, type(q))
        print(int(q))

        if q is not None:
            queryset = queryset.filter(product_verify=q)
        
        print(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

    @action(methods=['get'], detail=True)
    def get_images(self, request, pk):
        product = self.get_object()
        images =  product.product_imagess.all()
        serializer = ProductImagesSerializer(images, many=True)
        return Response(data=serializer.data, status=200)
    




    
    # def get_queryset(self):
    #     # Fetch all products
    #     queryset = ProductInformation.objects.all()

    #     # Sort in-memory by the product_added_time field from the serializer
    #     sort_by = self.request.query_params.get('sort_by', 'asc')
    #     products_with_time = []
        
    #     for product in queryset:
    #         serializer = self.get_serializer(product)
    #         products_with_time.append(serializer.data)

    #     # Now sort the list of dictionaries
    #     products_with_time.sort(key=lambda x: x['product_added_time'], reverse=(sort_by == 'desc'))

    #     return products_with_time
    
class AdminProductimagesAPI(viewsets.ModelViewSet):
    serializer_class = ProductImagesSerializer
    queryset = ProductImages.objects.all()
    http_method_names = ['get']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
