from decimal import Decimal
from django.conf import settings

from product.models import Product, Product_options

from collections import defaultdict

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        cart_ids = self.cart.keys()

        cart_values = self.cart.values()

        product_ids=[]
        product_sizes=[]

        for cart_value in cart_values:
            product_ids.append(cart_value['product_id'])
            product_sizes.append(cart_value['opt_size'])

        products = Product.objects.filter(id__in=product_ids)


        for i in range(len(products)):
            cart_id=str(products[i].id)+str(product_sizes[i])
            self.cart[str(cart_id)]['product'] = products[i]

        for item in self.cart.values():
            item['sell_price'] = Decimal(item['price']) + Decimal(item['opt_price'])
            item['total_price'] = item['sell_price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False, opt_size='', opt_price=0):
        product_id = product.id
        cart_id = str(product_id) + str(opt_size)
        if cart_id not in self.cart:
            self.cart[cart_id] = {'product_id':product.id ,
                                  'quantity':0,
                                  'price':str(product.price),
                                  'opt_size': opt_size,
                                  'opt_price':str(opt_price)
                                  }

        if is_update:
            self.cart[cart_id]['quantity'] = quantity
        else:
            self.cart[cart_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product, cart_id):
        product_id = str(product.id)
        if cart_id in self.cart:
            del(self.cart[cart_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True

    def get_product_total(self,call='test'):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return self.get_product_total()