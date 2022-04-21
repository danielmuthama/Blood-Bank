from tkinter import PIESLICE
from django.shortcuts import render, redirect


from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm

from donor.models import Donor, Hospital, BloodRequest, BloodDrive

# Create your views here.


# Helper function to request blood

def request_blood(request):
    # Grab the donor's email
    # Grab the hospital's email
    # Construct the email with the blood type and hospital contact info
    # Send the email to the donor

    pass


def home(request):

    blood_requests = BloodRequest.objects.all()
    return render(request, 'home.html', {'blood_requests': blood_requests})


def hos_signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # create hospital obj
            hos = Hospital(user=user)
            hos.save_hospital()

            messages.success(request, "Registration successful.")
            return redirect(hos_login)

        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/signup-hos.html", context={"register_form": form})


def hos_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(home)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    login_form = AuthenticationForm()

    return render(request=request, template_name="registration/login-hos.html", context={"login_form": login_form})


def don_signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            don = Donor(user=user)
            don.save_donor()

            messages.success(request, "Registration successful.")
            return redirect(don_login)

        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/signup-donor.html", context={"register_form": form})


def don_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(home)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    login_form = AuthenticationForm()

    return render(request=request, template_name="registration/login-donor.html", context={"login_form": login_form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect(home)


def hos_create_blood_drive(request):
    if request.method == 'POST':
        # Check if authenticated user is a hospital user obj
        hospital = Hospital.objects.get(user=request.user)
        if not hospital:
            return redirect('home')

        if request.method == 'POST':
            user = request.user
            blood_group = request.POST['blood_group']
            amount_wanted = request.POST['amount_wanted']

            blood_drive = BloodDrive(
                user=user, blood_group=blood_group, amount_wanted=amount_wanted)
            blood_drive.save()

            return redirect(home)

    return render(request, 'hos/create_blood_drive.html')


def don_apply_to_donate(request):
    # Check if authenticated user is a donor user obj
    if request.method == 'POST':
        donor = Donor.objects.get(user=request.user)
        if not donor:
            return redirect('home')

        if request.method == 'POST':
            user = request.user
            blood_group = request.POST['blood_group']
            age = request.POST['age']

            blood_request = BloodRequest(
                user=user, blood_group=blood_group, age=age)
            blood_request.save()

            return render(request, 'home.html')
    return render(request, 'don/apply_to_donate.html')
