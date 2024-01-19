from django.db import models
from customer.models import Customer
from orders.models import Orders
from deliveryboy.models import Deliveryboy
# Create your models here.
class Assign(models.Model):
    assign_id = models.AutoField(primary_key=True)
    # customer_id = models.IntegerField(blank=True, null=True)
    # customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # order_id = models.IntegerField(blank=True, null=True)
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)
    # deliveryboy_id = models.IntegerField(blank=True, null=True)
    deliveryboy=models.ForeignKey(Deliveryboy,on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'assign'


