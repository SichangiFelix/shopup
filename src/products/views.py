from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView
from . import models

# Create your views here.
class ProductListView(ListView):
    queryset = models.Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView,self).get_context_data(*args, **kwargs)
    #     return context

def product_list_view(request):
    queryset = models.Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/list.html", context)

class ProductDetailView(ListView):
    queryset = models.Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        return context

def product_detail_view(request, pk = None, *args, **kwargs):
    instance = models.Product.objects.get(pk = pk)
    #instance = get_object_or_404(models.Product, pk = pk)
    context = {
        "object": instance
    }
    return render(request, "products/detail.html", context)