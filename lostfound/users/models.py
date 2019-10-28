from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, registration_no, email, password=None):

        
        if not registration_no:
            raise ValueError('A valid registration number is required!')
        if not email:
            raise ValueError('A valid email address must be given!')

        user = self.model(
            registration_no=registration_no,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, registration_no, email, password):
        user = self.create_user(
            registration_no,
            email,
            password=password,
            )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Stratizen(AbstractBaseUser):
    registration_no = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50, unique=True)

    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'registration_no'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.registration_no)
        
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin