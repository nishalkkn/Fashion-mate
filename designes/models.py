from django.db import models

# Create your models here.
class Designes(models.Model):
    designe_id = models.AutoField(primary_key=True)
    designes = models.CharField(max_length=45)
    images = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'designes'
