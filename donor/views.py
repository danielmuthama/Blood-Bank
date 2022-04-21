from django.shortcuts import render
from .models import Donor, Hospital
from .serializers import DonorSerializer, HospitalSerializer
from rest_framework import viewsets


class DonorSerializerView(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer


class HospitalSerializerView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class DonorView(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer


class HospitalView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
