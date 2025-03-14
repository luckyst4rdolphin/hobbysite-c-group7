from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    '''
    Represents a category or type of product.
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
    '''
    name = models.CharField(max_length = 255)
    product_type = models.ForeignKey(
        ProductType,
        default = 1,
        on_delete = models.SET_NULL,
        null = True,
        related_name = "products"
    )
    description = models.TextField()
    price = models.DecimalField(max_digits = 50, decimal_places = 2)

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
        return reverse('merchstore:merch_detail', args=[self.pk])