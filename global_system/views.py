from statistics import quantiles
from django.shortcuts import render,redirect,get_object_or_404
from.models import Food, Booking, Table,Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import BookingForm,ReviewForm,DeliveryForm
from django.contrib.auth.decorators import login_required


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

    quantity = int(request.POST.get('quantity', 1))

    if str(food_id) in cart:
        cart[str(food_id)] += quantity
    else:
        cart[str(food_id)] = quantity

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

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'global_system/food_detail.html',{
        'food': food
    })


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            table = booking.table
            booking.total_price = table.table_price
            booking.save()
            return redirect('table_list_view')
    else:
        form = BookingForm()

    return render(request, 'global_system/book_table.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all().order_by('-id')
    return render(request, 'global_system/review_list.html', {'reviews': reviews})

@login_required
def leave_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'global_system/leave_review.html', {'form': form})

def buy(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')
    foods = Food.objects.filter(id__in=cart.keys())
    cart_items = []
    cart_total = 0
    for food in foods:
        quantity = cart[str(food.id)]
        item_total = food.price * quantity
        cart_items.append({
            'food': food,
            'quantity': quantity,
            'item_total': item_total
        })
        cart_total += item_total
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = DeliveryForm()
    context = {
        'form': form,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'total_delivery': cart_total,
    }

    return render(request, 'global_system/delivery.html', context)