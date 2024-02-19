from django.views.generic import ListView

from .models import Companie

class CompanieListView(ListView):
    model = Companie