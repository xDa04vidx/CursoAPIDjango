from django.contrib import admin
from django.urls import path
from patients.views import patients, detail_patient

urlpatterns = [
    path('patients', patients),
    path('patients/<int:pk>/', detail_patient),
]
