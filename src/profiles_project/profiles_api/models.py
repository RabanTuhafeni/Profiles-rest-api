from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User


# Create your models here.

class UserProfileManager(BaseUserManager):
    #**Helps Django work with our custom user model.***

    def create_user(self,email,name,password=None):
        #***creates a new user profile object.***

        if not email:
            raise ValueError('Users must have an email address.')

            email = self.normalize_email(email)
            user = self.model(email=email, name=name)

            user.set_password(password)
            user.save(using=self._db)

            return user
    #def blah(args):
        #User.objects.create_superuser(username='admin', password='123', email='admin@gmail.com')
    def create_superuser(self, email, name, password):
        if not email:
            raise ValueError('Users must have an email address.')

            username = self.normalize_email(username)
            user = self.model(email=email, name=name)

            user.set_password(password)
            user.save(using=self._db)

            return user
        #***Creates and saves a new superuser with given details.***

        #User =self.create_user(email, name, password)

        #User.is_superuser = True
        #User.is_staff = True

        #User.save(using=self._db)



class UserProfile(AbstractBaseUser, PermissionsMixin):
    #***Represents a "user profile" inside our system.***

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #***used to get a users full name. ***

        return self.name

    def get_short_name(self):
        #***used to get a users short name. ***

        return self.name

        def __str__(self):
            #***Django uses this when it needs to convert the object to a string ***

            return self.email

class ProfileFeedItem(models,Models):
    ***Profile Status Update.**

    user_profile = models.ForeignKey('UserProfile',on_delete = models.CASCADE)
    status_text = models.CharField(max_length=255)
    create_on = models.DateTimeField(auto_now_add=Time)

    def__str__(self):
    ***Return the model as a string.***

    return self,status_text
