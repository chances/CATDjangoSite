from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class person(models.Model):

    def __unicode__(self):
        return self.cat_username

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mcecs_username = models.CharField(max_length=50)
    pdx_username = models.CharField(max_length=50)
    cat_username = models.CharField(max_length=50)
    preferred_email = models.CharField(max_length=50)

