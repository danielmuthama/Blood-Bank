from django.shortcuts import render, redirect

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
    return render(request, 'home.html')


def hos_create_blood_drive(request):
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

    return render(request, 'hos/reate_blood_drive.html')


def don_apply_to_donate(request):
    # Check if authenticated user is a donor user obj
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
