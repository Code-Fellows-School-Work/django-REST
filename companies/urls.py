from django.urls import path
from .views import CompanieListView

urlpatterns =[
    path('', CompanieListView.as_view(), name='home'),
]