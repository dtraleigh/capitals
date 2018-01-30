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
    #Capitals visited so far
    us_capitals = Capital.objects.exclude(us_state='')

    #Capitals outside the US
    other_capitals = Capital.objects.filter(us_state='')

    #All visited capitals
    all_capitals = Capital.objects.all()
    all_photos = Photo.objects.all()

    #Calculate the progress so far
    us_capitals_visited = us_capitals.count()
    us_capitals_visited_percent = (us_capitals_visited / 50 ) * 100

    us_states_list = create_us_states_list()

    num_columns = 4
    all_columns = []

    if len(us_states_list) % num_columns == 0:
        # Equal column lengths
        col = 0
        start = 0
        end = len(us_states_list) / num_columns
        while (col < num_columns):
            this_col = us_states_list[start:end]

            start += len(us_states_list) / num_columns
            end += len(us_states_list) / num_columns
            col += 1
            all_columns.append(this_col)
    else:
        # Unequal column lengths
        rem = len(us_states_list) % num_columns
        col = 0
        start = 0
        end = int(len(us_states_list) / num_columns)
        while (col < num_columns):
            if rem > 0:
                this_col = us_states_list[int(start):int(end + 1)]
                start += int((len(us_states_list) / num_columns)) + 1
                end += int((len(us_states_list) / num_columns)) + 1
                rem -= 1
            else:
                this_col = us_states_list[int(start):int(end)]
                start += len(us_states_list) / num_columns
                end += len(us_states_list) / num_columns

            col += 1
            all_columns.append(this_col)

    return render(request, 'index.html', {'us_capitals':us_capitals,
                                        'all_photos':all_photos,
                                        'all_capitals':all_capitals,
                                        'us_capitals_visited':us_capitals_visited,
                                        'us_capitals_visited_percent':us_capitals_visited_percent,
                                        'us_states_list':us_states_list,
                                        'other_capitals':other_capitals,
                                        'all_columns':all_columns,
                                        'num_columns':num_columns})

def debug(request):
    us_states_list = create_us_states_list()

    return render(request, 'debug.html', {'us_states_list': us_states_list})

