from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from product.models import Product
from user.models import Account
from .forms import AddProductForm
from .cart import Cart

@require_POST
def add(request, product_id):
    cart = Cart(request)

    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

    cart_id=str(product_id)+cd['opt_size']

    product = get_object_or_404(Product, id=product_id)

    # form = AddProductForm(request.POST)


    cart.add(product=product,
             quantity=cd['quantity'],
             is_update=cd['is_update'],
             opt_size=cd['opt_size'],
             opt_price=cd['opt_price'])

    return redirect('cart:detail')

def remove(request, cart_id):
    cart = Cart(request)
    product_id=cart[cart_id]['product_id']
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product, cart_id)
    return redirect('cart:detail')

def detail(request):
    # 카카오톡 토큰
    context={}
    if request.session.get('access_token'):
        context['check'] = True

    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'],
                                                           'is_update':True,
                                                           'opt_size':product['opt_size'],
                                                           'opt_price':product['opt_price']
                                                           })
    context['cart']=cart


    return render(request, 'cart.html', context)