from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Person(models.Model):

    def __unicode__(self):
        return self.cat_username

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mcecs_username = models.CharField(max_length=50, blank=True, null=True)
    pdx_username = models.CharField(max_length=50)
    cat_username = models.CharField(max_length=50)
    cat_handle  = models.CharField(max_length=50)
    preferred_email = models.CharField(max_length=50)
    number_of_missed_mettings = models.IntegerField(default = 0)
    number_of_no_call = models.IntegerField(default = 0)
    strikes = models.IntegerField(default = 0)
    availability_flag =  models.BooleanField(default=False)
    dog_flag = models.BooleanField(default= True)
    dedog_flag = models.BooleanField(default = False)
    archived_dog_flag = models.BooleanField(default = False)
    alt_dog_flag = models.BooleanField(default = False)
    notes = models.CharField(max_length =140)
    num_of_absent_hr = models.IntegerField(default = 0)
    num_of_made_up_hr = models.IntegerField(default = 0)
    num_of_no_call_hr = models.IntegerField(default = 0)

class Shift(models.Model):
    user_id = models.ForeignKey(Person)

    start_date_and_time = models.DateTimeField()

    end_date_and_time = models.DateTimeField()
    expiry_date = models.DateField()

    dropped_flag = models.BooleanField(default = False)
    missed_flag = models.BooleanField(default = False)

class Availability(models.Model):
    user_id = models.ForeignKey(Person)


    start_date_and_time = models.DateTimeField()

    end_date_and_time = models.DateTimeField()

    effective_date = models.DateField()

class Holiday(models.Model):
    name = models.CharField(max_length = 40)
    date = models.DateField()
