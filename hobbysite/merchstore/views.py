from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Product, ProductType
from .forms import ProductForm, TransactionForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect


class MerchListView(ListView):
    '''
    View for displaying a list of product types and their associated products.
    '''
    model = Product
    template_name = 'merchstore_list.html'
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
    form_class = TransactionForm
    template_name = 'merchstore_detail.html'
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_type"] = self.object.product_type
        context["form"] = TransactionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.buyer = request.user.profile
            transaction.product = self.object
            
            if transaction.product.stock >= transaction.amount:
                transaction.product.stock -= transaction.amount
                if transaction.product.stock == 0:
                    transaction.product.status = "Out of Stock"
                transaction.product.save()
            
                transaction.status = "On cart"
                transaction.save()
                return redirect(reverse("merchstore:merch_detail", args=[self.object.pk]))
            else:
                form.add_error('amount', "Not enough stock available.")
        return self.render_to_response(self.get_context_data(form=form))

class MerchCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore_create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user.profile
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merchstore:merch_list')