from django.urls import path
from seller.api import *


urlpatterns = [
    path('product/',ProductInfoCreateView.as_view()),
    path('product/<pk>/',ProductRetrieveView.as_view()),
    path('prodCategory/',ProductCategoryListView.as_view()),
    path('prodImage/',ProductImageCreateView.as_view()),
    
]