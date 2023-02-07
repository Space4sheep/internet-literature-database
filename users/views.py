from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method != 'POST':
        # Показати порожню форму.
        form = UserCreationForm()
    else:
        # Опрацювати заповнену форму.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Аворизувати користувача та скерувати його на головну сторінку.
            login(request, new_user)
            return redirect('main:home')

    # Показати порожню або недійсну форму.
    return render(request, 'registration/register.html', {'form': form})

