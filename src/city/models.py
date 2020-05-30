from django.db import models
from src.province.models import Province

class City(models.Model):
    class Meta:
        db_table = 'city'

    name = models.CharField(max_length=50, null=False, blank=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, blank=True, editable=False)