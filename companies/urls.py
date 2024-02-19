from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns =[
    path('companies/', views.CompanieDetailView.as_view()),
    path('companies/<int:pk>/', views.CompanieDetailView.as_view())
]