from django import forms
from .models import Appointment


class DateInput(forms.DateInput):
    input_type= 'date'
    

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        
        widgets= {
            'date': DateInput(),
        }
        