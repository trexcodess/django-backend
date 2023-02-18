from django.db import models
from django.utils.timezone import get_current_timezone

class Reservation(models.Model):
    first_name = models.CharField(max_length=50, default='First name')
    last_name = models.CharField(max_length=50, default='Last name')
    email = models.EmailField(max_length=120, default='Email')
    age = models.CharField(max_length=2, default="25")
    
    city = models.CharField(max_length=100, default="New York")
    state = models.CharField(max_length=2, default="NY")
    zipcode = models.CharField(max_length=5, default='90210')
    url = models.URLField(default='https://example.com')
    
    created_date = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    other =models.TextField(blank=True, null=True)
  
   
    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        ordering = ['-created_date']
   
  