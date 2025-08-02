from django.db import models

class AdminBoundary(models.Model):
    name_0 = models.CharField(max_length=100)  # Country
    name_1 = models.CharField(max_length=100)  # State
    name_2 = models.CharField(max_length=100)  # District
    name_3 = models.CharField(max_length=100, null=True, blank=True)  # Taluk (if available)

    class Meta:
        db_table = 'ind_adm13'
        