from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=40)
    main_text = models.TextField()
    image = models.ImageField(upload_to="images/")
    pub_time = models.DateTimeField(auto_now_add=True)
