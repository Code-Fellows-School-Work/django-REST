from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import CompanieListView, CompanieDetailView

urlpatterns =[
    path('', CompanieListView.as_view(), name="company_list"),
    path('<int:pk>/', CompanieDetailView.as_view(), name="company_detail"),
]