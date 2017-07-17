from django.test import TestCase

from capitals.views import create_us_states_list

class capitals_info_check(TestCase):

    def test_output_info(self):
        us_states_list = create_us_states_list()

        print(us_states_list)

