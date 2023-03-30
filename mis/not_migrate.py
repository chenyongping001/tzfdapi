from django.db import models


class EmployeePhone(models.Model):
    ygdm = models.CharField(primary_key=True, max_length=55)
    ygmc = models.CharField(max_length=55)
    sjhm = models.CharField(max_length=55)
    dhhm = models.CharField(max_length=55, blank=True, null=True)
    bgdh = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_cyp_ygsj'
