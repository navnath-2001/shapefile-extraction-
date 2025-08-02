from django.contrib.gis.db import models  # Use GeoDjango for geometry field

class ind_adm2(models.Model):
    gid = models.AutoField(primary_key=True)
    id_0 = models.FloatField(null=True, blank=True)
    iso = models.CharField(max_length=3, null=True, blank=True)
    name_0 = models.CharField(max_length=75, null=True, blank=True)
    id_1 = models.FloatField(null=True, blank=True)
    name_1 = models.CharField(max_length=75, null=True, blank=True)
    id_2 = models.FloatField(null=True, blank=True)
    name_2 = models.CharField(max_length=75, null=True, blank=True)
    type_2 = models.CharField(max_length=50, null=True, blank=True)
    engtype_2 = models.CharField(max_length=50, null=True, blank=True)
    nl_name_2 = models.CharField(max_length=100, null=True, blank=True)
    varname_2 = models.CharField(max_length=100, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        db_table = 'ind_adm2'
   
