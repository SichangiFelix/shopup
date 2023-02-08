from django.shortcuts import render
from django.views import ListView
from . import models

# Create your views here.
class ProductListView(ListView):
    queryset = models.Product.objects.all()

def product_list_view(request):
    queryset = models.Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product/product_list_view.html", context)