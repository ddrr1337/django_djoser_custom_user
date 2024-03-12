from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
import random




class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
    
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        Profile.objects.create(user=user)
      

        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        # is_active in True for testing
        extra_fields.setdefault(
            "is_active", True
        ) 
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True) 
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
    
    def generate_activation_code(self):
  
        return str(random.randint(10000, 99999))



class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(unique=True)
    

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()




class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)





def user_directory_path(instance, filename):

    return f'user_{instance.user.id}/{filename}'



    




