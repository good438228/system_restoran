from statistics import quantiles

from django.shortcuts import render,redirect,get_object_or_404
from.models import Food, Booking, Table
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import BookingForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'global_system/register.html', {'form': form})

def food_list(request):
    search_query = request.GET.get('search', '')
    foods = Food.objects.all()

    if search_query:
        foods = foods.filter(name__icontains=search_query)

    return render(request, 'global_system/food_list.html',{
        'foods': foods
    })

def cart_view(request):
    cart = request.session.get('cart', {})

    cart_foods = []
    total_price = 0

    for food_id, quantity in cart.items():
        food = Food.objects.get(id=food_id)
        item_total = food.price * quantity
        cart_foods.append({
            'food': food,
            'quantity': quantity,
            'total_price': item_total
        })
        total_price += item_total

    return render(request, 'global_system/cart.html', {
        'cart_foods': cart_foods,
        'total_price': total_price
    })

def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    cart = request.session.get('cart', {})

    cart[str(food_id)] = cart.get(str(food_id), 0) + 1
    request.session['cart'] = cart

    return redirect('cart_view')


def remove_from_cart(request, food_id):
    cart = request.session.get('cart', {})
    food_id_str = str(food_id)

    if food_id_str in cart:
        if cart[food_id_str] > 1:
            cart[food_id_str] -= 1
        else:
            del cart[food_id_str]

        request.session['cart'] = cart

    return redirect('cart_view')


def table_view(request):
    tables = Table.objects.all()
    return render(request, 'global_system/table_list.html', {
        'tables': tables
    })

def table_detail(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    return render(request, "global_system/table_detail.html", {
        'table': table
    })