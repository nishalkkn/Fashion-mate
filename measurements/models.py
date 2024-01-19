from django.db import models
from customer.models import Customer
class Measurements(models.Model):
    mesherment_id = models.AutoField(primary_key=True)
    # customer_id = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    neck = models.CharField(db_column='Neck', max_length=45)  # Field name made lowercase.
    shoulder = models.CharField(db_column='Shoulder', max_length=45)  # Field name made lowercase.
    bust = models.CharField(db_column='Bust', max_length=45)  # Field name made lowercase.
    shoulder_to_bust = models.CharField(db_column='Shoulder to Bust', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    under_bust = models.CharField(db_column='Under Bust', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    full_sleeve_length = models.CharField(db_column='Full sleeve length', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    half_sleeve_length = models.CharField(db_column='Half sleeve length', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bicep = models.CharField(db_column='Bicep', max_length=45)  # Field name made lowercase.
    shoulder_to_hip = models.CharField(db_column='Shoulder to hip', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    waist = models.CharField(db_column='Waist', max_length=45)  # Field name made lowercase.
    hip = models.CharField(db_column='Hip', max_length=45)  # Field name made lowercase.
    waist_to_knee = models.CharField(db_column='Waist to knee', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    knee = models.CharField(db_column='Knee', max_length=45)  # Field name made lowercase.
    inseam = models.CharField(db_column='Inseam', max_length=45)  # Field name made lowercase.
    thigh = models.CharField(db_column='Thigh', max_length=45)  # Field name made lowercase.
    cuff = models.CharField(max_length=45)
    way = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'measurements'


# Create your models here.
# class Measurements(models.Model):
#     mesherment_id = models.AutoField(primary_key=True)
#     mesherments = models.CharField(max_length=45, blank=True, null=True)
#     # customer_id = models.IntegerField()
#     customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
#
#     class Meta:
#         managed = False
#         db_table = 'measurements'
