from django.forms import ModelForm
from .models import staffdetails
from django import forms


class newStaff(forms.Form):
	
	class Meta:

		model = staffdetails

		fields = ('staff_fname','staff_lname','staff_sex','staff_mobile','staff_id','staff_password')