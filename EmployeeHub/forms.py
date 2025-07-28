from django.forms import ModelForm
from .models import *
from .views import *

class Employee_Form(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'