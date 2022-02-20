from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting_type = request.GET.get('sort', 'id')
    template = 'catalog.html'
    phone_obj = Phone.objects.all()
    phones = []
    context = {}
    for phone in phone_obj:
        phone_dict = {}
        phone_dict['id'] = phone.id
        phone_dict['name'] = phone.name
        phone_dict['price'] = phone.price
        phone_dict['image'] = phone.image
        phone_dict['slug'] = phone.slug
        phones.append(phone_dict)
    print(sorting_type)
    if sorting_type == 'name':
        phones = sorted(phones, key=lambda i:i['name'])
    elif sorting_type == 'id':
        phones = sorted(phones, key=lambda i:i['id'])
    elif sorting_type == 'min_price':
        phones = sorted(phones, key=lambda i:i['price'])
    elif sorting_type == 'max_price':
        phones = sorted(phones, key=lambda i:i['price'], reverse=True)
    context['phones'] = phones
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_obj = Phone.objects.filter(slug=slug)
    for phone in phone_obj:
        phone_details = {}
        phone_details['name'] = phone.name
        phone_details['price'] = phone.price
        phone_details['image'] = phone.image
        phone_details['release_date'] = phone.release_date
        phone_details['lte_exists'] = phone.lte_exists
    context = {
        'phone': phone,
    }
    return render(request, template, context)
