from django.db import models

# Create your models here.


class consumer(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=20)
    bank = models.DecimalField(max_digits=5, decimal_places=2)


class items(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

