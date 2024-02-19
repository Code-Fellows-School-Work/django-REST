from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Companie
from .serializers import CompanieSerializer

class CompanieListView(ListCreateAPIView):
    queryset = Companie.objects.all()
    serializer_class = CompanieSerializer

class CompanieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Companie.objects.all()
    serializer_class = CompanieSerializer