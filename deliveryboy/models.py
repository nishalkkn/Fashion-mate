from django.db import models

# Create your models here.
class Deliveryboy(models.Model):
    deliveryboy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'deliveryboy'
