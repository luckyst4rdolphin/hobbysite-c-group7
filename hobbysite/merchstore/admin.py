from django.contrib import admin
from .models import Product, ProductType, Transaction


class ProductTypeAdmin(admin.ModelAdmin):
    '''
    Admin configuration for ProductType model
    '''
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class ProductTypeInline(admin.StackedInline):
    '''
    Inline configuration for ProductType within Product admin
    '''
    model = ProductType
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    '''
    Admin configuration for Product model
    '''
    list_display = ('name', 'product_type', 'price')
    list_filter = ('product_type',)
    search_fields = ('name', 'product_type__name')

class TransactionAdmin(admin.ModelAdmin):
    '''
    Admin configuration for Product model
    '''
    list_display = ('buyer', 'product', 'amount', 'status')
    list_filter = ('product',)
    search_fields = ('buyer', 'product__name')

# Register models with their corresponding admin configurations
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
