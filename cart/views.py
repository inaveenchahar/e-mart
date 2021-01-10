from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Cart, CartProduct
from accounts.models import UserAddress
from accounts.forms import UserAddressForm
from products.models import Category, Product
from django.contrib import messages

from payments.models import Order, Payment
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings
# Create your views here.


def cart_product(request, p_slug, id):
    """
        adds product to the cart
    """
    product = get_object_or_404(Product, slug=p_slug, id=id, visible=True)
    if request.user.is_authenticated:
        """
            checks if a cart is already created for user or not.
            if not then it creates a new empty cart
        """
        if Cart.objects.filter(completed=False, user=request.user):
            cart = Cart.objects.get(completed=False, user=request.user)
        else:
            cart = Cart.objects.create(user=request.user)

        """
            checks if product is in cart or not
            if not then adds the product to the cart
        """
        if CartProduct.objects.filter(cart=cart, product=product):
            c_product = CartProduct.objects.get(cart=cart, product=product)
        else:
            c_product = CartProduct.objects.create(
                cart=cart,
                product=product,
                price=product.discounted_price,
                quantity=0
            )
        """
            checks whether product quantity is not exceeds the limit set by seller for maximum product quntity
        """
        if c_product.quantity > product.buy_limit:
            messages.warning(request, "You can only add maximum {quantity} of this product".format(quantity=product.buy_limit))
            return redirect('product:product_details', product.slug, product.id)
        c_product.quantity += 1
        c_product.save()
        messages.success(request, "You have successfully added {prdt} in your cart.".format(prdt=product))
        return redirect('product:product_details', product.slug, product.id)
    messages.warning(request, "Login/Sing up to add this product in your cart")
    return redirect('product:product_details', product.slug, product.id)


# def cart_product(request, c_slug, p_slug, id):
#     category = get_object_or_404(Category, slug=c_slug)
#     product = get_object_or_404(Product, slug=p_slug, id=id)
#     p_quantity = 1
#     if request.method == 'POST':
#         p_quantity = request.POST.get('p_quantity')
#         if int(p_quantity) < 1:
#             p_quantity = 1
#     if request.user.is_authenticated:
#         if Cart.objects.filter(completed=False, user=request.user):
#             cart = Cart.objects.get(completed=False, user=request.user)
#         else:
#             cart = Cart.objects.create(user=request.user)
#         if CartProduct.objects.filter(cart=cart, product=product):
#             c_product = CartProduct.objects.get(cart=cart, product=product)
#         else:
#             c_product = CartProduct.objects.create(
#                 cart=cart,
#                 product=product,
#                 price=product.price,
#                 quantity=0
#             )
#         c_product.quantity += int(p_quantity)
#         c_product.save()
#         messages.success(request, "You have successfully added {prdt} in your cart.".format(prdt=product))
#         return redirect('main:homepage')
#     return render(request, 'product_details.html', {'category': category, 'product': product})


def increase_quantity(request, cp_id):
    """
        increases the cart product quantity by 1
    """
    if request.user.is_authenticated:
        c_product = get_object_or_404(CartProduct, id=cp_id)
        product = Product.objects.get(id=c_product.product.id)
        if c_product.quantity >= product.buy_limit:
            messages.warning(request, "You can only add maximum {quantity} of this product".format(quantity=product.buy_limit))
            return redirect('cart:view_cart')
        else:
            c_product.quantity += 1
            c_product.save()
            return redirect('cart:view_cart')
    else:
        messages.warning(request, "Login/Sing up to perform this action")
        return redirect('cart:view_cart')


def decrease_quantity(request, cp_id):
    """
        decreases the cart product quantity by 1.
        if the quantity is 1 then it can't be decreased
    """
    if request.user.is_authenticated:
        c_product = get_object_or_404(CartProduct, id=cp_id)
        if c_product.quantity > 1:
            c_product.quantity -= 1
            c_product.save()
            return redirect('cart:view_cart')
        else:
            messages.error(request, 'Quantity must be 1 or more than 1')
            return redirect('cart:view_cart')
    else:
        messages.warning(request, "Login/Sing up to perform this action")
        return redirect('cart:view_cart')


def remove_cart_product(request, cp_id):
    """
        deletes the product from the cart
    """
    if request.user.is_authenticated:
        c_product = get_object_or_404(CartProduct, id=cp_id)
        c_product.delete()
        messages.info(request, "Product removed from cart successfully")
        return redirect('cart:view_cart')
    else:
        messages.warning(request, "Login/Sing up to perform this action")
        return redirect('main:homepage')


# def update_cart(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.get(completed=False, user=request.user)
#         if request.method == 'POST':
#             try:
#                 product = cart.cartproduct_set.get(pk=request.POST['product'])
#                 p_quantity = int(request.POST['p_quantity'])
#                 if p_quantity < 1:
#                     prod = CartProduct.objects.get(id=product.id)
#                     prod.delete()
#                     return redirect('cart:view_cart')
#             except (KeyError, CartProduct.DoesNotExist):
#                 return HttpResponse("error occurred")
#             else:
#                 product.quantity = p_quantity
#                 product.save()
#                 return redirect('cart:view_cart')
#     else:
#         return HttpResponse("Login to update your cart")


def view_cart(request):
    """
        displays active cart product and other cart information
    """
    if request.user.is_authenticated:
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False, product__visible=True).count()

        if tcp > 0:
            """
                update the cart total value and check if there any delivery charge applicable or not,
                if product price, delivery charges are changed then it will update cart cart automatically
            """
            cart = Cart.objects.filter(completed=False, user=request.user).last()
            cart_products = CartProduct.objects.filter(cart=cart)
            total = 0
            for item in cart_products:
                total = total + (item.quantity * item.product.discounted_price)
                item.price = item.product.discounted_price
                item.save()
            cart.cart_value = total
            """
                check the cart value and compares it with free delivery over seller specified free cart delivery
            """
            if cart.cart_value > settings.CART_VALUE:
                cart.delivery_charges = 0
            else:
                cart.delivery_charges = settings.DELIVERY_CHARGE
            cart.save()
            return render(request, 'view_cart.html',{'cart': cart, 'cart_products': cart_products, 'tcp': tcp, 'total': total})
        else:
            empty_cart_message = 'Your cart is empty. Add products to it.'
            return render(request, 'view_cart.html', {'empty_cart_message': empty_cart_message, 'tcp': tcp})
    else:
        tcp = 0
        return render(request, 'view_cart.html', {'tcp': tcp})








# def view_cart(request):
#     if request.user.is_authenticated:
#         tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False, product__visible=True).count()
#
#         if tcp > 0:
#             cart = Cart.objects.filter(completed=False, user=request.user).last()
#             cart_products = CartProduct.objects.filter(cart=cart)
#             total = 0
#             for item in cart_products:
#                 total = total + (item.quantity * item.product.price)
#             cart.cart_value = total
#             cart.save()
#             ud_address = UserAddress.objects.filter(user=request.user, default_address=True).last()
#
#             address_form = UserAddressForm(request.POST or None)
#             total_address = UserAddress.objects.filter(user=request.user).count()
#             if total_address >= 6:
#                 address_form = None
#             return render(request, 'view_cart.html', {'cart': cart, 'cart_products': cart_products, 'tcp': tcp, 'total': total, 'ud_address': ud_address, 'address_form': address_form, 'total_address': total_address})
#         else:
#             empty_cart_message = 'Your cart is empty. Add products to it.'
#             return render(request, 'view_cart.html', {'empty_cart_message': empty_cart_message, 'tcp': tcp})
#     else:
#         tcp = 0
#         return render(request, 'view_cart.html', {'tcp': tcp})
