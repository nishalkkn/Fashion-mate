from django.db import models
from customer.models import Customer
# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    # customer_id = models.IntegerField(blank=True, null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'feedback'
