from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    type_sort = request.GET.get('sort')
    match type_sort:
        case 'max_price':
            phones = Phone.objects.all().order_by('price')
        case 'min_price':
            phones = Phone.objects.all().order_by('-price')
        case 'name':
            phones = Phone.objects.all().order_by('name')
        case _:
            phones = Phone.objects.all()
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
