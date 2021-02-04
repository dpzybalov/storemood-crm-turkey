from django.shortcuts import render
from .models import PhotoSessions, PhotoSessionsImage, PhotoTool
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def is_member(user):
    return user.groups.filter(name='Member').exists()


@login_required(login_url='/')
def index_photo(request):
    if request.user.groups.filter(id='1').exists():
        photosessionslist = PhotoSessions.objects.filter(user=request.user)
    else:
        photosessionslist = PhotoSessions.objects.all()
    print(request)
    return render(request, 'photo/index.html', {'PhotoSessions': photosessionslist})


@login_required(login_url='/')
def add_photosession(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        city = request.POST.get('City')
        boat = request.POST.get('Boat')

        photosessions = PhotoSessions.objects.create(
            title = '1'
        )

        for file_num in range(0, int(length)):
            PhotoSessionsImage.objects.create(
                Photosessions= photosessions,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'photo/add_photosession.html')


@login_required(login_url='/')
def equipment_list(request):
    tool = PhotoTool.objects.filter(owner=request.user)
    return render(request, 'photo/equipment_list.html', {'tool': tool})
