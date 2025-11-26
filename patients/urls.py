from django.contrib import admin
from django.urls import path
from patients.views import ListPatientsView, DetailPatientView
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet

router = DefaultRouter()
router.register('patients',PatientViewSet)

urlpatterns =  router.urls
