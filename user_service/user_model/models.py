from django.contrib.auth.models import User
from django.db import models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.CharField(max_length=11, unique=True, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=50, blank=True)
    fullname = models.TextField()

    class Meta:
        db_table ="profile"

    def __str__(self):
        return '%s %s %s %s %s' % (self.fullname, self.user.username, self.
                                      address, self.phone, self.gender)

