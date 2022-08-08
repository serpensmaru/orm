from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def if_parameter_sort(get_parameter):
    if get_parameter == "name":
        parameter = Phone.objects.order_by('name')
        return parameter
    elif get_parameter == "min_price":
        parameter = Phone.objects.order_by('price')
        return parameter
    elif get_parameter == "max_price":
        parameter = Phone.objects.order_by('-price')
        return parameter
    else:
        parameter = Phone.objects.all()
        return parameter


def show_catalog(request):  # sort = name, min_price, max_price
    template = 'catalog.html'
    parameter = request.GET.get('sort')
    phones = if_parameter_sort(parameter)
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_slug = Phone.objects.filter(slug=slug)
    phone = [x for x in phone_slug]
    context = {"phone": phone[0]}
    return render(request, template, context)
