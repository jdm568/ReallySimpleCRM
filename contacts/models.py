from django.db import models
from datetime import datetime

class Contact(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)
    address_line_1 = models.CharField(max_length = 100,  default="")
    address_line_2 = models.CharField(max_length = 100,  default="")
    city = models.CharField(max_length = 100,  default="")
    state = models.CharField(max_length = 100, default="")
    zipcode = models.CharField(max_length = 100,  default="")
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name