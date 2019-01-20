import us

from django.shortcuts import render
from capitals.models import Capital, Photo


def create_us_states_list():
    # Get a list of all the capitals in the format ('city name', 0/1, 'XX')
    # The city name is the name of the capital,
    # 0 is for not visited, 1 is for visited,
    # 'XX' is the state code.
    us_states_list = []
    us_states_choices = Capital._meta.get_field('us_state').choices

    for state in us_states_choices:
        capital = []
        capital.append(us.states.lookup(state[0]).capital + ', ' + state[0])

        if Capital.objects.filter(us_state=state[0]).exists():
            capital.append(True)
        else:
            capital.append(False)

        capital.append(state[0])

        us_states_list.append(capital)

    return us_states_list


def home(request):
    # Capitals outside the US
    other_capitals = Capital.objects.filter(us_state='')

    # All visited capitals
    all_capitals = Capital.objects.all()
    all_photos = Photo.objects.all()

    # Calculate the progress so far
    us_capitals_visited = Capital.objects.exclude(us_state='').count()
    us_capitals_visited_percent = (us_capitals_visited / 50) * 100

    us_states_list = create_us_states_list()

    # Returns list of state names that we have visited
    # ["Indiana", "North Carolina", ....]
    us_visited_states = []

    us_state_objects = [s for s in Capital.objects.exclude(us_state='')]
    for us_state_object in us_state_objects:
        us_visited_states.append(us.states.lookup(us_state_object.us_state).name)

    return render(request, 'index.html', {'all_photos': all_photos,
                                          'all_capitals': all_capitals,
                                          'us_capitals_visited': us_capitals_visited,
                                          'us_capitals_visited_percent': us_capitals_visited_percent,
                                          'us_states_list': us_states_list,
                                          'other_capitals': other_capitals,
                                          'us_visited_states': us_visited_states})


def debug(request):
    # Just playing around
    us_states_list = create_us_states_list()

    list_of_us_state_objects = us.states.STATES

    # US Capitals visited so far
    us_capitals = Capital.objects.exclude(us_state='')

    # Returns list of state names that we have visited
    # ["Indiana", "North Carolina", ....]
    us_visited_states = []

    us_state_objects = [s for s in Capital.objects.exclude(us_state='')]
    for us_state_object in us_state_objects:
        us_visited_states.append(us.states.lookup(us_state_object.us_state).name)

    return render(request, 'debug.html', {'us_states_list': us_states_list,
                                          'list_of_us_state_objects': list_of_us_state_objects,
                                          'us_capitals': us_capitals,
                                          'us_visited_states': us_visited_states})

