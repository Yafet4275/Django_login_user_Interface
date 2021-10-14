from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User             #Clase basica de usuario y se va a editar
from django.contrib.auth.models import PermissionsMixin             #
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):                          #Usar el modelo de django personalizado
    def create_user(self, email, name, password=None):              #User profile manager 
        if not email:
            raise ValueError('Email is requirited')

        email=self.normalize_email(email)                           #convert from capital to lowercase
        user=self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)                                   #Make sure password is in hash       
        return user

    def create_superuser(self, email, name, password):              #Admin user profile
        user=self.create_user(email, name, password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Modelo base de datos para usuarios en el sistema
    email=models.EmailField(max_length=255, unique=True)            #Unique means that is a unique field
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)                     #El usuario que es creado va hacer activo
    is_staff=models.BooleanField(default=False)                     #Saber si son miembro del equipo
    
    objects=UserProfileManager()                                    #Usar el modelo de django personalizado
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        return self.name                                            #Get full name 

    def get_short_name(self):
        return self.name                                            #Get short name

    def __str__(self):
        return self.email                                           #Return string represent username