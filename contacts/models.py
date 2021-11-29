from django.db import models

# Create your models here.
from JASIRI_SIMULATION_TEST.metadata import MetaData
from accounts.models import User


class Contact(MetaData):
    firstName= models.CharField(verbose_name='first Name', max_length=100)
    lastName= models.CharField(verbose_name='Last Name', max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    class Meta:
        db_table = "contact"


class ContactPhone(MetaData):
    phone = models.CharField( max_length=100)
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE,default=None)
    class Meta:
        db_table="contact_phone"



class ContactEmail(MetaData):
    email = models.CharField(max_length=100)
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE,default=None)
    class Meta:
        db_table="contact_email"
