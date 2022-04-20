from django.shortcuts import render
from .models import Donor,Hospital,User
from .serializers import DonorSerializer,HospitalSerializer,UserSerializer
from rest_framework import viewsets

class DonorSerializerView(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
class HospitalSerializerView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
class UserSerializerView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer        

