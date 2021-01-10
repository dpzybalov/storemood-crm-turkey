from django.shortcuts import redirect
from django.shortcuts import render
from .form import UserLoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from photo.models import PhotoTool


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/photo')
    else:
        form = UserLoginForm()

    if request.user.is_authenticated:
        return redirect('/photo')
    else:
        return render(request, 'login/index.html', {'form': form})


@login_required(login_url='/')
def user_profile(request):
    tool = PhotoTool.objects.all()

    return render(request, 'login/profile.html', {'tool': tool})


@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('/')
