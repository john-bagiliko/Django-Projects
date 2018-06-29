"""
By: Bagiliko John
Year: 2018
""" 
from django.db import models

class School(models.Model):
	name=models.CharField(max_length=80, unique=True)
	email=models.EmailField()
	address_and_info=models.TextField()
	image=models.ImageField(blank=True, null=True)
	marked = models.BooleanField(default=False)

	def __str__(self):
		return self.name


	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url
