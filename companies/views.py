from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Companie
from .serializers import CompanieSerializer

class CompanieListView(ListCreateAPIView):
    queryset = Companie.objects.all() # using queryset because it is a collection of things or in this case, companies
    serializer_class = CompanieSerializer # this takes all the company instances and converts to JSON

class CompanieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Companie.objects.all()
    serializer_class = CompanieSerializer