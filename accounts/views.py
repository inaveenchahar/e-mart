from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, UserAddress
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm, UserAddressForm
from cart.models import CartProduct
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            new_user = User.objects.create_user(
                first_name=instance.first_name,
                last_name=instance.last_name,
                username=instance.username,
                email=instance.email,
                password=instance.password
            )
            login(request, new_user)
            messages.success(request, 'You have successfully signed up as {name}.'.format(name=new_user.username))
            return redirect('main:homepage')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.error(request, 'You are logged out now.')
        return redirect('main:homepage')
    else:
        return redirect('main:homepage')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged as {name}.'.format(name=user.username))
            return redirect('main:homepage')
    else:
        form = LoginForm()
    return render(request, 'login_view.html', {'form': form})


def manage_addresses(request):
    if request.user.is_authenticated:
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False, product__visible=True).count()
        all_addresses = UserAddress.objects.filter(user=request.user)
        if request.method == "POST":
            address_form = UserAddressForm(request.POST)
            if address_form.is_valid():
                for adres in UserAddress.objects.filter(user=request.user):
                    adres.default_address = False
                    adres.save()
                instance = address_form.save(commit=False)
                instance.default_address = True
                instance.user = request.user
                instance.save()
                return redirect('accounts:manage_addresses')
        else:
            address_form = UserAddressForm()
        if all_addresses.count() > 6:
            address_form = None
        return render(request, 'manage_addresses.html', {'all_addresses': all_addresses, 'address_form': address_form, 'tcp': tcp})
    else:
        return redirect('main:homepage')


def delete_address(request, id):
    if request.user.is_authenticated:
        address = get_object_or_404(UserAddress, id=id)
        address.delete()
        if UserAddress.objects.filter(user=request.user):
            if not UserAddress.objects.filter(user=request.user, default_address=True).count() > 0:
                address = UserAddress.objects.filter(user=request.user).last()
                address.default_address = True
                address.save()
        return redirect('accounts:manage_addresses')
    else:
        return redirect('main:homepage')


def select_default_address(request, id):
    if request.user.is_authenticated:
        for adres in UserAddress.objects.filter(user=request.user):
            adres.default_address = False
            adres.save()
        address = get_object_or_404(UserAddress, id=id)
        address.default_address = True
        address.save()
        return redirect('accounts:manage_addresses')
    else:
        return redirect('main:homepage')


def update_address(request, id):
    if request.user.is_authenticated:
        address = get_object_or_404(UserAddress, id=id)
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False, product__visible=True).count()
        if request.method == 'POST':
            update_adForm = UserAddressForm(request.POST, instance=address)
            if update_adForm.is_valid():
                update_adForm.save()
                return redirect('accounts:manage_addresses')
        else:
            update_adForm = UserAddressForm(instance=address)
        return render(request, 'update_address.html', {'address': address, 'update_adForm': update_adForm, 'tcp': tcp})
    else:
        return redirect('main:homepage')
