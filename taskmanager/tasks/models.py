# patient_data/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Existing models for patient data
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of Birth
    gender = models.CharField(max_length=10)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class EHRData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100, default='Default Doctor')
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"EHR for {self.patient.first_name} {self.patient.last_name}"

class WearableData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    heart_rate = models.IntegerField()
    steps = models.IntegerField()
    sleep_hours = models.FloatField()
    date = models.DateTimeField()

    def _str_(self):
        return f"Wearable data for {self.patient.first_name} {self.patient.last_name} on {self.date}"

class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    date = models.DateTimeField()

    def _str_(self):
        return f"{self.test_name} result for {self.patient.first_name} {self.patient.last_name}"

# New Insurance Model
class Insurance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    insurance_company = models.CharField(max_length=200)
    plan_type = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    coverage_details = models.TextField()
    valid_until = models.DateField()

    def _str_(self):
        return f"{self.patient.first_name} {self.patient.last_name} - {self.insurance_company}"

# New Pharmacy Model
class Pharmacy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    pharmacy_name = models.CharField(max_length=200)
    prescription_date = models.DateTimeField()
    refill_date = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return f"{self.medication_name} prescribed to {self.patient.first_name} {self.patient.last_name}"
    
 


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


    

