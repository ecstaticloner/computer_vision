from django.db import models
# Create your views here.

class Item(models.Model):
        SlNo=models.IntegerField()
        item=models.CharField(max_length=250)  
        description = models.CharField(max_length=250)
        
        def __str__(self):
            return '{}'.format(self.item)