from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ProductType(models.Model):
    '''
    Represents a category or type of product.
    It has name and description.
    '''
    name = models.CharField(max_length = 255)
    description = models.TextField()

    class Meta:
        '''
        Orders product types alphabetically by name and sets the plural name as "Product Types" in the Django admin.
        '''
        ordering = ['name',]
        verbose_name_plural = "Product Types"
    
    def __str__(self):
        '''
        Returns the name of the product type.
        '''
        return self.name

class Product(models.Model):
    '''
    Represents an individual product belonging to a specific product type.
    It has the following fields: name, product_type, owner, description, price, stock, and status.
    '''
    STATUS_CHOICES = [
        ("Available", "Available"),
        ("On sale", "On sale"),
        ("Out of Stock", "Out of Stock"),
    ]
    name = models.CharField(max_length = 255)
    product_type = models.ForeignKey(
        ProductType,
        default = 1,
        on_delete = models.SET_NULL,
        null = True,
        related_name = "products"
    )
    owner = models.ForeignKey(
        Profile,
        null = True,
        on_delete = models.CASCADE  
    )
    description = models.TextField()
    price = models.DecimalField(max_digits = 50, decimal_places = 2)
    stock = models.PositiveIntegerField(default = 0)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = "Available"
    )

    class Meta:
        '''
        Orders products alphabetically by name.
        '''
        ordering = ['name']
    
    def __str__(self):
        '''
        Returns the name of the product.
        '''
        return self.name
    
    def get_absolute_url(self):
        '''
        Returns the URL for the product's detail page.
        '''
        return reverse('merchstore:merch_detail', args = [self.pk])
    
    def save(self, *args, **kwargs):
        '''
        Automatically saves the product's status based on its stock before saving.
        '''
        if self.stock == 0:
            self.status = "Out of Stock"
        else:
            self.status = "Available"
        super().save(*args, **kwargs)
    
class Transaction(models.Model):
    '''
    Represents a transaction made by a buyer for a specific product.
    It has the following fields: buyer, product, amount, status, and created on.
    '''
    STATUS_CHOICES = [
        ("On cart", "On cart"),
        ("To Pay", "To Pay"),
        ("To Ship", "To Ship"),
        ("To Receive", "To Receive"),
        ("Delivered", "Delivered"),
    ]

    buyer = models.ForeignKey(
        Profile,
        null = True,
        on_delete = models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        null = True,
        on_delete = models.SET_NULL
    )
    amount = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES
    )
    created_on = models.DateTimeField(auto_now_add=True)