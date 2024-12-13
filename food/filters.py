from django_filters import rest_framework as filters

from food.models import Dish

class DishTypeFilter(filters.FilterSet):

    type = filters.MultipleChoiceFilter(choices=Dish.TYPE_CHOICES)