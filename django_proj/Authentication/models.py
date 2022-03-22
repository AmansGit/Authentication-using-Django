from django.db import models
from phone_field import PhoneField

# Create your models here.
class Authentication(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone_number = PhoneField()
	email = models.EmailField(max_length=250)
	password = models.CharField(max_length=50)

	class Meta:
		db_table = 'user_authentication'