"""
By: Bagiliko John
Year: 2018
""" 

from django import forms 
from .models import School
class AddSchoolForm(forms.ModelForm):
	
	class Meta:
		model = School
		fields=[
		"name",
		"image",
		"address_and_info",
		"email",
		"marked"
		]
   