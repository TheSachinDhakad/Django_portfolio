from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    # phone = models.CharField(max_length=12)
    subject = models.TextField()
    massage = models.TextField( null=True)
    date = models.DateField()


    def __str__(self):
        return self.name