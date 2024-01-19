from django.db import models

# Create your models here.

class Materials(models.Model):
    material_id = models.AutoField(primary_key=True)
    materials = models.CharField(max_length=45)
    uplod_image = models.CharField(db_column='uplod image', max_length=500, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'materials'

