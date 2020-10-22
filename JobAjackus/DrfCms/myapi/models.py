from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.
#list of categories
Categorylist = [
    ('null', '--'),
    ('Mystery','Mystery'),
    ('Fiction','Fiction'),
    ('Fantasy','Fantasy')
]

# Create your models here.

class customuser(AbstractUser):
    username = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
       

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)
        

class contentcreater(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
     related_name='profile')  
    id = models.IntegerField(primary_key=True, unique=True)
    #email = models.EmailField(primary_key=True, unique=True)
    fullname =models.CharField(max_length = 60)
    #password = models.CharField(max_length = 8) #add uppercase adn lowercase calidation ********???
    phone = models.IntegerField(max_length = 10 )
    phone1 = models.IntegerField(max_length = 10, null=True, blank=True )
    address =models.CharField(max_length = 100 ,null=True, blank=True)
    city =models.CharField(max_length = 50 ,null=True, blank=True)
    state =models.CharField(max_length = 50 ,null=True, blank=True)
    country =models.CharField(max_length = 50 ,null=True, blank=True)
    pincode = models.IntegerField(max_length = 10 )
    def __str__(self):
        return self.fullname
    

# the content class defines the structure of the content object and inturn 
# tbl that will be used to store the listings from the users
class content(models.Model):
    title = models.CharField(max_length = 30, unique=True, blank=False)
    body = models.CharField(max_length = 200)
    summary = models.CharField(max_length = 60)
    #document= pdf uplaod ?????*****
    category = models.CharField(choices = Categorylist, default = '--', max_length = 50)
    creater = models.ForeignKey(contentcreater, related_name='contents',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
   

  
 