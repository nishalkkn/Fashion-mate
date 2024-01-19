from django.db import models

# Create your models here.
class Designers(models.Model):
    designers_id = models.AutoField(primary_key=True)
    designers_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'designers'
