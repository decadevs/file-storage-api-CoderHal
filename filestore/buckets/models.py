from djongo import models
# from django.utils import timezone

# Create your models here.
class Bucket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return str(self.name)

    
