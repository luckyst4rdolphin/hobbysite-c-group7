from django import forms
from .models import Product, Transaction

class ProductForm(forms.ModelForm):
    '''
    Form for creating or updating a product.
    Excludes the 'owner' field, which is set automatically in the view.
    '''
    class Meta:
        model = Product
        exclude = ['owner']

class TransactionForm(forms.ModelForm):
    '''
    Form for creating a transaction.
    Restricts amount to a minimum value of 1.
    '''
    amount = forms.IntegerField(min_value=1)
    
    class Meta:
        model = Transaction
        fields = ['amount']