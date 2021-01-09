from django.shortcuts import render
from .models import PhotoSessions
from .forms import PhotosessionsForm, ClientForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.dateformat import DateFormat
from datetime import datetime, date


@login_required(login_url='/')
def is_member(user):
    return user.groups.filter(name='Member').exists()

@login_required(login_url='/')
def index_photo(request):
    if request.user.groups.filter(id='1').exists():
        PhotoSessionsList = PhotoSessions.objects.filter(user=request.user)
    else:
        PhotoSessionsList = PhotoSessions.objects.all()
    print(request)
    return render(request, 'photo/index.html', {'PhotoSessions': PhotoSessionsList})


@login_required(login_url='/')
def add_photosession(request):
    if request.method == 'POST':
        print('POST ЗАПРОС')
        form1 = PhotosessionsForm(request.POST)
        form2 = ClientForm(request.POST)
        if form1.is_valid():
            PhotoSessions = form1.save()
            PhotoSessions.user = request.user.username
            today = datetime.today()
            PhotoSessions.title = today.strftime("%m.%d.%Y") + str(form1.instance.boat)

            PhotoSessions.save()

            return redirect('/photo')
        if form1.is_valid() == False:
            return redirect('/index.html')

    else:
        form1 = PhotosessionsForm()
        form2 = ClientForm(request.POST)
    return render(request, 'photo/add_photosession.html', {'form1': form1, 'form2': form2})