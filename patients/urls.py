from django.contrib import admin
from django.urls import path
from patients.views import ListPatientsView, detail_patient

urlpatterns = [
    path('patients', ListPatientsView.as_view()),
    path('patients/<int:pk>/', detail_patient),
]
