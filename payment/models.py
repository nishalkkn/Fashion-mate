from django.db import models
from orders.models import Orders
from customer.models import Customer

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # order_id = models.IntegerField(blank=True, null=True)
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)
    # customer_id = models.IntegerField(blank=True, null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'

