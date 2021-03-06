from djongo import models

# Create your models here.
class Bucket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return str(self.name)

    
