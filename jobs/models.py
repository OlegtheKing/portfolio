from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to="images/")  # upload_to is for save folder to be specified, inside of main media folder
    summary = models.CharField(max_length=200)  # restriction to the length of a string