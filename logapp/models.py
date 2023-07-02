# Create your models here.
from django.db import models


class UserLog(models.Model):
    user_id = models.IntegerField(db_index=True)
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=255,null=True,blank=True)
    event_time_stamp = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_log'