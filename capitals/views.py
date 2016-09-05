from django.shortcuts import render

from capitals.models import Capital, Photo

def home(request):
    us_capitals = Capital.objects.exclude(us_state='')
    all_photos = Photo.objects.all()

    return render(request, 'index.html', {'us_capitals':us_capitals,
                                        'all_photos':all_photos})
