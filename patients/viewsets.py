from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PatientSerializer
from .models import Patient

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @action(["GET"], detail=True, url_path="set-name")
    def custom_operation(self, request,pk):
        patient = self.get_object()
        if patient.first_name == "David":
            patient.first_name = "Juan"
        patient.save()
        return Response("Nombre modificado")
