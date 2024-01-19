from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    adress = models.CharField(max_length=100)
    pincode = models.CharField(max_length=45)
    house_name = models.CharField(db_column='house name', max_length=45)  # Field renamed to remove unsuitable characters.
    landmark = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'customer'
