from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class MerchListView(ListView):
    '''
    View for listing all products in merchandise store.
    '''
    model = Product
    template_name = 'merchstore_list.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        '''
        Returns the queryset of products, excluding the user's own products if authenticated.
        '''
        user = self.request.user
        if user.is_authenticated:
            return Product.objects.exclude(owner=user.profile)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        '''
        Adds extra context data to the template: all product types, list of user products if authenticated, and URL for creating a new product.
        '''
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['product_types'] = ProductType.objects.all()
        context['create_product_url'] = reverse('merchstore:merch_create')

        if user.is_authenticated:
            context['user_products'] = Product.objects.filter(owner=user.profile)
        else:
            context['user_products'] = []

        return context

class MerchDetailView(DetailView):
    '''
    View for displaying details of a single product.
    Allows users to buy a product.
    '''
    model = Product
    form_class = TransactionForm
    template_name = 'merchstore_detail.html'
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        '''
        Adds product type and transaction form to the context.
        '''
        context = super().get_context_data(**kwargs)
        context["product_type"] = self.object.product_type
        context["form"] = TransactionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        '''
        Handles the form submission for creating a transaction.
        Verifies the stock availability and updates product status.
        '''
        self.object = self.get_object()
        form = TransactionForm(request.POST)

        if not request.user.is_authenticated:
            return redirect('login')
        
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

class MerchCreateView(LoginRequiredMixin, CreateView):
    '''
    View for creating a new product. Requires the user to be authenticated.
    '''
    model = Product
    form_class = ProductForm
    template_name = 'merchstore_create.html'

    def form_valid(self, form):
        '''
        Handles the valid form submission, sets the product owner, and sets its status based on stock.
        '''
        product = form.save(commit=False)
        product.owner = self.request.user.profile
        if product.stock == 0:
            product.status = "Out of Stock"
        else:
            product.status = "Available"
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        '''
        Redirects to the product list page after successfully creating a product.
        '''
        return reverse_lazy('merchstore:merch_list')

class MerchUpdateView(LoginRequiredMixin, UpdateView):
    '''
    View for updating an existing product. Requires the user to be authenticated.
    '''
    model = Product
    form_class = ProductForm
    template_name = 'merchstore_update.html'

    def form_valid(self, form):
        '''
        Handles the valid form submission, and updates the product's status based on stock.
        '''
        product = form.save(commit=False)
        if product.stock == 0:
            product.status = "Out of Stock"
        else:
            product.status = "Available"
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        '''
        Redirects to the product list page after successfully updating a product.
        '''
        return reverse_lazy('merchstore:merch_detail', args=[self.object.pk])

class MerchCartView(LoginRequiredMixin, ListView):
    '''
    View for displaying a list of items in the user's shopping cart. Requires the user to be authenticated.
    '''
    model = Transaction
    template_name = 'merchstore_cart.html'
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        '''
        Adds the list of cart items for the current user to the context.
        '''
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile
        context['cart_items'] = Transaction.objects.filter(buyer=user_profile).order_by('product__owner')
        return context

class MerchTransactionView(LoginRequiredMixin, ListView):
    '''
    View for displaying a list of transactions related to products the user is selling. Requires the user to be authenticated.
    '''
    model = Transaction
    template_name = 'merchstore_transaction.html'
    context_object_name = 'transaction_items'

    def get_context_data(self, **kwargs):
        '''
        Adds the list of transactions for products the user owns to the context.
        '''
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile
        context['transaction_items'] = Transaction.objects.filter(product__owner=user_profile).order_by('buyer')
        return context