from django.contrib import admin
from .models import ProductImages, ProductInformation, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(ProductInformation)
admin.site.register(ProductImages)