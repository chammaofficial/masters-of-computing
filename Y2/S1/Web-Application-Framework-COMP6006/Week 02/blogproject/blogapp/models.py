from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    tag =  models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def is_pre_covid_post(self):
        return self.publish_date <= datetime.date(2020,3,10)

