from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, ProductType

class MerchListView(ListView):
    '''
    View for displaying a list of product types and their associated products.
    '''
    model = Product
    template_name = 'merch_list.html'
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_types"] = ProductType.objects.prefetch_related("products")
        return context


class MerchDetailView(DetailView):
    '''
    View for displaying details of a single product.
    '''
    model = Product
    template_name = 'merch_detail.html'
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_type"] = self.object.product_type
        return context