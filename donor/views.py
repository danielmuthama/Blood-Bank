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


def home(request):
    return render(request, 'home.html')


def hos_request_blood(request):
    return render(request, 'hos/request_blood.html')


def hos_create_blood_drive(request):
    return render(request, 'hos/reate_blood_drive.html')


def don_apply_to_donate(request):
    return render(request, 'don/apply_to_donate.html')
class DonorView(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
class HospitalView(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
