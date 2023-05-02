from django.db import models

# Create your models here.

class Sync(models.Model):
    id = models.AutoField(primary_key=True)
    sync = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'sync'
