from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# An event or incident for the diary each complaining resident
# keeps on anti social behaviour
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description= models.TextField(null=True, blank=True)
# the finished value means that the resident has finished the entry
# and will no longer edit it
    finished = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
# the seen_by means that the HA rep has seen the entry
    seen_by = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['finished']