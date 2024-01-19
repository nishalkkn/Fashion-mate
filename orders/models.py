from django.db import models
from customer.models import Customer
from models.models import Models
# Create your models here.

class Orders(models.Model):
    orders_id = models.AutoField(primary_key=True)
    quantity = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(db_column='STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # customer_id = models.CharField(max_length=45, blank=True, null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # model_id = models.CharField(max_length=45, blank=True, null=True)
    model=models.ForeignKey(Models,on_delete=models.CASCADE)
    working_status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'
