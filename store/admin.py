from django.contrib import admin
from .models import Carousel, Category,  Product, ProductImages, Location

# Register your models here.


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']


@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']
