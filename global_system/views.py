from django.shortcuts import render,redirect,get_object_or_404
from.models import Food
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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