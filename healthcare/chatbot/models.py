"""
Models for the Healthcare Assistant.
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class HealthLog(models.Model):
    """Model for storing health logs."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    log_type = models.CharField(
        max_length=50,
        choices=[
            ('symptom', 'Symptom'),
            ('medication', 'Medication'),
            ('appointment', 'Appointment'),
            ('vital', 'Vital Sign'),
            ('exercise', 'Exercise'),
            ('diet', 'Diet'),
            ('other', 'Other'),
        ],
        default='other'
    )
    severity = models.CharField(
        max_length=20,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('critical', 'Critical'),
        ],
        default='medium'
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return f"{self.title} - {self.date_created.strftime('%Y-%m-%d')}"


class MedicationReminder(models.Model):
    """Model for medication reminders."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(
        max_length=50,
        choices=[
            ('daily', 'Daily'),
            ('twice_daily', 'Twice Daily'),
            ('three_times_daily', 'Three Times Daily'),
            ('weekly', 'Weekly'),
            ('as_needed', 'As Needed'),
            ('custom', 'Custom'),
        ],
        default='daily'
    )
    time_of_day = models.TimeField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return f"{self.medication_name} - {self.frequency}"


class VitalSign(models.Model):
    """Model for vital signs."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    vital_type = models.CharField(
        max_length=50,
        choices=[
            ('blood_pressure', 'Blood Pressure'),
            ('heart_rate', 'Heart Rate'),
            ('temperature', 'Temperature'),
            ('weight', 'Weight'),
            ('blood_sugar', 'Blood Sugar'),
            ('oxygen_saturation', 'Oxygen Saturation'),
            ('respiratory_rate', 'Respiratory Rate'),
        ]
    )
    value = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    date_recorded = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date_recorded']
    
    def __str__(self):
        return f"{self.vital_type}: {self.value} {self.unit}"
