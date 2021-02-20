from upload.models import SendedTasks
from django.shortcuts import render, redirect
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


def all_students(request, group_id):
    all = [str(elem) for elem in list(Account.objects.filter(group = group_id).values_list('snumber', flat=True))]
    result = []
    
    for student in all:
        points = 0
        all_points = [int(elem) for elem in list(SendedTasks.objects.filter(snumber = student).values_list('max_point', flat=True))]
        for point in all_points:
            points += point
        result.append({'student':student,'points':points})
        Account.objects.filter(snumber = student).update(points = points)

    return render(request, 'users/group.html', {'result':result})

    