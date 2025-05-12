from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class MerchListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'merchstore_list.html'
    context_object_name = 'all_products'  # this will be all products except user's

    def get_queryset(self):
        # Exclude products owned by the logged-in user
        return Product.objects.exclude(owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile

        context['user_products'] = Product.objects.filter(owner=user_profile)
        context['product_types'] = ProductType.objects.prefetch_related('products')
        context['create_product_url'] = reverse('merchstore:merch_create')  # assumes named URL exists
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
                else:
                    transaction.product.status = "Available"
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
        if product.stock == 0:
            product.status = "Out of Stock"
        else:
            product.status = "Available"
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merchstore:merch_list')

class MerchUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore_update.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        if product.stock == 0:
            product.status = "Out of Stock"
        else:
            product.status = "Available"
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merchstore:merch_detail', args=[self.object.pk])

class MerchCartView(ListView):
    model = Transaction
    template_name = 'merchstore_cart.html'
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile

        context['cart_items'] = Transaction.objects.filter(buyer=user_profile).order_by('product__owner')
        return context

class MerchTransactionView(ListView):
    model = Transaction
    template_name = 'merchstore_transaction.html'
    context_object_name = 'transaction_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile

        context['transaction_items'] = Transaction.objects.filter(product__owner=user_profile).order_by('buyer')
        return context