
from django.db import models
from datetime import datetime
from django.core.validators import validate_slug





class staffdetails(models.Model):

	staff_fname = models.CharField(max_length=200)
	staff_lname = models.CharField(max_length=200)
	staff_sex = models.CharField(max_length=10)
	staff_mobile = models.CharField(max_length=200)
	staff_grade = models.CharField(max_length=200)
	staff_id = models.CharField(max_length=200)
	staff_password = models.CharField(max_length=200)

class patient(models.Model):
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	sex = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	zone = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	dob = models.CharField(max_length=200)
	pob = models.CharField(max_length=200)
	lga = models.CharField(max_length=200)
	plan = models.CharField(max_length=200)
	receipt = models.CharField(max_length=200)
	payment_type= models.CharField(max_length=200)
	amount = models.CharField(max_length=200)
	created = models.CharField(max_length=200)