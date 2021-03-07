from upload.models import SendedTasks, StudentsPoints
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            mo = re.compile(r'[0-9]{6}')
            check_snumber = form.cleaned_data['snumber']
            res = re.findall(mo, check_snumber)
            if not res:
                messages.warning(request, "Niepoprawny format numeru indeksu.")
            else:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Konto stworzone dla {username}!')
                return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if not request.user.is_staff:
        group = Group.objects.get(id = request.user.group_id)
    else:
        group = ''
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Pomyślnie zmieniono hasło!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/profile.html', {'group':group, 'form':form})


def groups(request):
    all = Group.objects.all()
    for group in all:
        print(group.group)
    return render(request, 'users/groups.html', {'all': all})

@staff_member_required(login_url='login')
def new_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            mo = re.compile(r'^[\w_\s]*$')
            check_name = form.cleaned_data['name']
            res = re.findall(mo, check_name)
            if not res:
                messages.warning(request, "Niepoprawna nazwa grupy.")
            else:
                mo_n = re.compile(r'[0-9]{4}\/[0-9]{4}')
                check_year = form.cleaned_data['year']
                res_n = re.findall(mo_n, check_year)
                if not res_n:
                    messages.warning(request, "Niepoprawny format daty.")
                else:
                    group = Group()
                    group.name = form.data['name']
                    group.year = form.data['year']
                    group.term = form.data['term']
                    group.save()
                    return redirect('all_groups')
    else:
        form = GroupForm()
    return render(request, 'users/new_group.html', {'form': form})

@login_required
def all_students(request, group_id):
    result = Account.objects.filter(group_id = group_id)
    return render(request, 'users/group.html', {'result':result})

    