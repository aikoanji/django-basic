from django.db import models

class Province(models.Model):
    class Meta:
        db_table = 'province'

    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, blank=True, editable=False)