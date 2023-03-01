from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterUserForm


def register(request):
    if request.method != 'POST':
        # Показати порожню форму.
        form = RegisterUserForm()
    else:
        # Опрацювати заповнену форму.
        form = RegisterUserForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Аворизувати користувача та скерувати його на головну сторінку.
            login(request, new_user)
            return redirect('main:home')

    # Показати порожню або недійсну форму.
    return render(request, 'registration/register.html', {'form': form})

