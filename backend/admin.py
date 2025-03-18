from django.contrib import admin
from.models import Product
from django import forms

class ProductAdminForm(forms.ModelForm):
    auction_duration = forms.CharField(help_text="Enter duration in HH:MM:SS format.")

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)