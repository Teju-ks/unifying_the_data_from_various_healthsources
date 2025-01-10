from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'tasks/login.html')

@login_required
def profile_view(request):
    return render(request, 'tasks/profile.html')

def signup(request):
    return render(request, 'tasks/signup.html')

def subscribe(request):
    return render(request, 'tasks/subscribe.html')

def about(request):
    return render(request, 'tasks/about.html')

def faq(request):
    return render(request, 'tasks/faq.html')

def contact(request):
    return render(request, 'tasks/contact.html')

def index(request):
    return render(request, 'tasks/base.html')

def create(request):
    return render(request, 'tasks/create.html')

def create_username_view(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('create_username')

        if User.objects.filter(username=userid).exists():
            messages.error(request, "User ID already exists.")
            return redirect('create_username')

        user = User.objects.create_user(username=userid, password=password)
        user.save()
        login(request, user)
        return redirect('subscribe')
    return render(request, 'tasks/create_username.html')

def subscription_view(request):
    return render(request, 'tasks/subscribe.html')

def patient_dashboard(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    
    # Get the latest data from EHR, wearable devices, lab results, insurance, and pharmacy
    ehr_data = EHRData.objects.filter(patient=patient).order_by('-last_updated').first()
    wearable_data = WearableData.objects.filter(patient=patient).order_by('-date').first()
    lab_results = LabResult.objects.filter(patient=patient).order_by('-date')[:5]
    insurance_data = Insurance.objects.filter(patient=patient).order_by('-valid_until').first()
    pharmacy_data = Pharmacy.objects.filter(patient=patient).order_by('-prescription_date')[:5]
    
    context = {
        'patient': patient,
        'ehr_data': ehr_data,
        'wearable_data': wearable_data,
        'lab_results': lab_results,
        'insurance_data': insurance_data,
        'pharmacy_data': pharmacy_data,
    }
    return render(request, 'tasks/dashboard.html', context)


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Sign up failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})
