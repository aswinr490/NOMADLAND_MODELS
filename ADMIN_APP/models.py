from django.db import models


class AdminModel(models.Model):
    admin_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'admin_data'