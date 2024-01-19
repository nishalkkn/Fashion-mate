from django.db import models
from materials.models import Materials
# Create your models here.


class Models(models.Model):
    models_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=45)
    uplode_image = models.CharField(max_length=400)
    # material_id = models.IntegerField()
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)
    amount = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    colour = models.CharField(max_length=45)



    class Meta:
        managed = False
        db_table = 'models'

