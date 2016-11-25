from django.views.generic import ListView
from carapp.core.models import Car


class CarView(ListView):
    model = Car
    template_name = 'core/car_list.html'
    context_object_name = 'cars'