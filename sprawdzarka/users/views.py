from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from .models import *

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Konto stworzone dla {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@staff_member_required(login_url='login')
def groups(request):
    all = Group.objects.all()
    return render(request, 'users/groups.html', {'all': all})

@staff_member_required(login_url='login')
def new_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group()
            group.name = form.data['name']
            group.year = form.data['year']
            group.term = form.data['term']
            group.save()
            return redirect('all_groups')
    else:
        form = GroupForm()
    return render(request, 'users/new_group.html', {'form': form})