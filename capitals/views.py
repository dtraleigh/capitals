from django.shortcuts import render

from capitals.models import Capital, Photo

def home(request):
    us_capitals = Capital.objects.exclude(us_state='')
    all_capitals = Capital.objects.all()
    all_photos = Photo.objects.all()

    us_capitals_visited = us_capitals.count()
    us_capitals_visited_percent = (us_capitals_visited / 50 ) * 100

    return render(request, 'index.html', {'us_capitals':us_capitals,
                                        'all_photos':all_photos,
                                        'all_capitals':all_capitals,
                                        'us_capitals_visited':us_capitals_visited,
                                        'us_capitals_visited_percent':us_capitals_visited_percent})
