from django.shortcuts import render,redirect,get_object_or_404
from.models import Food
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get("username")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'global_system/reqister.html', {"form": form})