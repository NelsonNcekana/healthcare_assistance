"""
Management command to create sample health data for demonstration.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from healthcare.chatbot.models import HealthLog, MedicationReminder, VitalSign


class Command(BaseCommand):
    """Class Command."""
    help = 'Creates sample health data for demonstration'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample health data...')

        # Create sample health logs
        health_logs_data = [
            {
                'title': 'Morning Headache',
                'description': (
                    'Experienced mild headache upon waking up. '
                    'Took ibuprofen and felt better after 30 minutes.'
                ),
                'log_type': 'symptom',
                'severity': 'low'
            },
            {
                'title': 'Blood Pressure Check',
                'description': (
                    'Routine blood pressure measurement. '
                    'Results within normal range.'
                ),
                'log_type': 'vital',
                'severity': 'low'
            },
            {
                'title': 'Exercise Session',
                'description': (
                    'Completed 30-minute cardio workout. '
                    'Felt energized and maintained good form throughout.'
                ),
                'log_type': 'exercise',
                'severity': 'low'
            },
            {
                'title': 'Medication Side Effect',
                'description': (
                    'Noticed slight dizziness after taking new medication. '
                    'Will monitor and report to doctor.'
                ),
                'log_type': 'medication',
                'severity': 'medium'
            },
            {
                'title': 'Doctor Appointment',
                'description': (
                    'Annual checkup scheduled for next week. '
                    'Need to prepare questions about new symptoms.'
                ),
                'log_type': 'appointment',
                'severity': 'low'
            }
        ]

        for log_data in health_logs_data:
            HealthLog.objects.create(**log_data)

        # Create sample medication reminders
        medications_data = [
            {
                'medication_name': 'Lisinopril',
                'dosage': '10mg',
                'frequency': 'daily',
                'time_of_day': timezone.now().time().replace(hour=8, minute=0),
                'start_date': date.today() - timedelta(days=30),
                'notes': 'Take with breakfast. Monitor blood pressure.'
            },
            {
                'medication_name': 'Metformin',
                'dosage': '500mg',
                'frequency': 'twice_daily',
                'time_of_day': timezone.now().time().replace(hour=8, minute=0),
                'start_date': date.today() - timedelta(days=60),
                'notes': 'Take with meals. Helps control blood sugar.'
            },
            {
                'medication_name': 'Ibuprofen',
                'dosage': '400mg',
                'frequency': 'as_needed',
                'start_date': date.today() - timedelta(days=10),
                'notes': (
                    'For pain relief. Take as needed, '
                    'not more than 4 times daily.'
                )
            }
        ]

        for med_data in medications_data:
            MedicationReminder.objects.create(**med_data)

        # Create sample vital signs
        vitals_data = [
            {
                'vital_type': 'blood_pressure',
                'value': '120/80',
                'unit': 'mmHg',
                'notes': 'Normal range. Measured in the morning.'
            },
            {
                'vital_type': 'heart_rate',
                'value': '72',
                'unit': 'bpm',
                'notes': 'Resting heart rate. Within normal range.'
            },
            {
                'vital_type': 'temperature',
                'value': '98.6',
                'unit': '°F',
                'notes': 'Normal body temperature.'
            },
            {
                'vital_type': 'weight',
                'value': '165',
                'unit': 'lbs',
                'notes': 'Stable weight. Measured weekly.'
            },
            {
                'vital_type': 'blood_sugar',
                'value': '95',
                'unit': 'mg/dL',
                'notes': 'Fasting blood sugar. Normal range.'
            }
        ]

        for vital_data in vitals_data:
            VitalSign.objects.create(**vital_data)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created sample data:\n'
                f'- {len(health_logs_data)} health logs\n'
                f'- {len(medications_data)} medication reminders\n'
                f'- {len(vitals_data)} vital signs'
            )
        )
