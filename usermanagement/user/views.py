import pdb

from django.shortcuts import render, redirect, HttpResponse
from .models import user_details


def home_page(request):
    return render(request, 'welcome.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = user_details.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            return redirect('userprofile')
        except user_details.DoesNotExist:
            return HttpResponse('Invalid username or password')

    return render(request, 'loginpage.html')


def signup_page(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        uname = request.POST['username']
        psw = request.POST['password']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        city = request.POST['city']

        if user_details.objects.filter(username=uname).exists():
            message = "Username already exists. Please choose a different username."
            return render(request, 'signuppage.html', {'message': message})

        user_details.objects.create(
            fullname=name,
            username=uname,
            password=psw,
            gender=gender,
            birthdate=birthdate,
            city=city
        )
        return redirect('signupsuccess')

    return render(request, 'signuppage.html')


def signup_success(request):
    return render(request, 'signupsuccess.html')


def user_profile(request):
    user_id = request.session.get('user_id')
    try:
        user = user_details.objects.get(id=user_id)
    except user_details.DoesNotExist:
        return HttpResponse('User not found')

    return render(request, 'userprofile.html', {'user': user})


def edit_profile(request):
    user_id = request.session.get('user_id')
    user = user_details.objects.get(id=user_id)

    if request.method == 'POST':
        user.fullname = request.POST['fullname']
        user.password = request.POST['password']
        user.gender = request.POST['gender']
        user.birthdate = request.POST['birthdate']
        user.city = request.POST['city']
        user.save()
        return redirect('userprofile')

    return render(request, 'editprofile.html', {'user': user})

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')











def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'admin125' and password == 'admin125':
            request.session['is_admin'] = True
            return redirect('manage_users')
        else:
            return HttpResponse('Invalid credentials.')

    return render(request, 'login_admin.html')


def logout_admin(request):
    if 'is_admin' in request.session:
        del request.session['is_admin']
    return redirect('home')



def admin_manage_users(request):
    if 'is_admin' not in request.session or not request.session['is_admin']:
        return HttpResponse('You are not authorized to view this page.')

    users = user_details.objects.all()
    return render(request, 'manage_users.html', {'users': users})


def edit_user(request, user_id):
    if 'is_admin' not in request.session or not request.session['is_admin']:
        return HttpResponse('You are not authorized to view this page.')

    user = user_details.objects.get(id=user_id)

    if request.method == 'POST':
        user.fullname = request.POST['fullname']
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.gender = request.POST['gender']
        user.birthdate = request.POST['birthdate']
        user.city = request.POST['city']
        user.save()
        return redirect('manage_users')

    return render(request, 'edit_user.html', {'user': user})


def delete_user(request, user_id):
    if 'is_admin' not in request.session or not request.session['is_admin']:
        return HttpResponse('You are not authorized to view this page.')

    user = user_details.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('manage_users')

    return render(request, 'delete_user.html', {'user': user})


