from django.db import models
#from django.db.models.fields import CharField, URLField
#from django.db.models.fields.files import ImageField
import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/iamges/')
    date = models.DateField(datetime.date.today)

    def __str__(self):
        return self.title + ' - ' + self.description