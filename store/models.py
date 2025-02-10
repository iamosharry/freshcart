from django.db import models

# Create your models here.


class Carousel(models.Model):
    image = models.ImageField(upload_to='uploads/carousel/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Category(models.Model):
    title = models.CharField(max_length=100)

    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+", blank=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subcategories',
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    CURRENCY = '₦'

    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.BooleanField(default=False)
    discount_price = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='category')

    def __str__(self):
        return str(self.title)

    def formatted_price(self):
        return f'{self.CURRENCY}{int(self.price):,}'

    def get_discounted_price(self):
        if self.discount:
            return self.discount_price
        return self.price


class ProductImages(models.Model):
    image = models.ImageField(upload_to='uploads/product/')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name_plural = 'ProductImages'


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, default='Nigeria')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
