import us

from django.shortcuts import render
from capitals.models import Capital, Photo

def home(request):
    #Get some information to start with
    us_capitals = Capital.objects.exclude(us_state='')
    all_capitals = Capital.objects.all()
    all_photos = Photo.objects.all()

    #Calculate the progress so far
    us_capitals_visited = us_capitals.count()
    us_capitals_visited_percent = (us_capitals_visited / 50 ) * 100

    #Get a list of all the capitals in the format ('city name', 0/1)
    #The city name is the name of the capital,
    #0 is for not visited, 1 is for visited.
    us_states_list = []
    us_states_choices = Capital._meta.get_field('us_state').choices
    for state in us_states_choices:
        capital = []
        city = us.states.lookup(state[0]).capital
        capital.append(us.states.lookup(state[0]).capital + ', ' + state[0])

        if Capital.objects.filter(us_state=state[0]).exists():
            capital.append(True)
        else:
            capital.append(False)

        us_states_list.append(capital)

    return render(request, 'index.html', {'us_capitals':us_capitals,
                                        'all_photos':all_photos,
                                        'all_capitals':all_capitals,
                                        'us_capitals_visited':us_capitals_visited,
                                        'us_capitals_visited_percent':us_capitals_visited_percent,
                                        'us_states_list':us_states_list})
