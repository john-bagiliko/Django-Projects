"""
By: Bagiliko John
Year: 2018
""" 

from django import forms 
from .models import School
class AddSchoolForm(forms.ModelForm):
	# address_and_info=forms.CharField(required=False, help_text='please enter the address and further information this school')
	class Meta:
		model = School
		fields=[
		"name",
		"image",
		"address_and_info",
		"email",
		"marked"
		]
   