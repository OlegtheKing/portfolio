from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=40)
    main_text = models.TextField()
    image = models.ImageField(upload_to="images/")
    pub_time = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.main_text[:50] + ".."

    def pub_time_short(self):
        return self.pub_time.strftime("%b %e %Y")

    def __str__(self):  # the name used whenever django-adm displays object
        return self.heading
