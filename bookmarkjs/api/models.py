from django.db import models
from django.contrib.auth.models import User


# django admin user 
# uses email and password field tp create user
class User(User):
    pass


# folder model 
# have a title and the user which it belongs to
class Folder(models.Model):
    title       = models.CharField(max_length=256)
    user        = models.OneToOneField(User,on_delete=models.CASCADE,related_name="folders",unique=True)
    
# book mark model 
# url to the page book marked
# user it belongs to 
# folder it befongs to
class BookmarkPage(models.Model):
    url         =  models.URLField()
    Title       = models.CharField(null=True,blank=True,max_length=256)
    user        = models.OneToOneField(User,on_delete=models.CASCADE,related_name="bookmarks",unique=True)
    folder      = models.ForeignKey(Folder,on_delete=models.CASCADE,related_name="content",null=True)

