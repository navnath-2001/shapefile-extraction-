from django.contrib.gis.db import models

class ind_adm3(models.Model):
    gid = models.AutoField(primary_key=True)
    id_0 = models.IntegerField()
    name_0 = models.CharField(max_length=100)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=100)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=100)
    id_3 = models.IntegerField()
    name_3 = models.CharField(max_length=100)
    type_3 = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)  # Adjust SRID if needed

    class Meta:
        db_table = 'ind_adm3'
