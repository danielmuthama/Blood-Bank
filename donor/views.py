from django.shortcuts import render
from .models import Donor, Hospital, User


''''

Views to be rendered as API endpoints

'''


''''

Views to handle requests from the front end

'''


def home(request):
    return render(request, 'home.html')


def hos_request_blood(request):
    return render(request, 'hos/request_blood.html')


def hos_create_blood_drive(request):
    return render(request, 'hos/reate_blood_drive.html')


def don_apply_to_donate(request):
    return render(request, 'don/apply_to_donate.html')
