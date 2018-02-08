from django.db import models
from jsonfield import JSONField


class Risk(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    fields = JSONField(null=True, blank=True)
    
    def __str__(self):
        return '%s' %self.title


class DataStore(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='data')
    data_dump = JSONField(null=True, blank=True)