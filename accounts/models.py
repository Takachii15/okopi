from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model



class UserManager(BaseUserManager):
# create user function
    def create_user(self, email, username, full_name, password=None):
        if not email:
            raise ValueError('User harus memiliki email')
        if not full_name:
            raise ValueError('Tolong masukkan nama lengkap anda')
        if not username:
            raise ValueError('Tolong masukkan username anda')

        user = self.model(
                email = self.normalize_email(email),
                username = username,
                full_name = full_name,
                )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # create admin function
    def create_superuser(self, email, username, full_name, password, *args, **kwargs):
        user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                full_name = full_name,
                password=password,
                )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user






class User(AbstractBaseUser):

    # custom user model
    email        = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username     = models.CharField(verbose_name="username", max_length=60, unique=True)
    full_name    = models.CharField(verbose_name="nama lengkap", max_length=255)
    disp         = models.ImageField(upload_to='photos/disp/%Y%m/%d/')
    adress       = models.TextField(verbose_name='alamat', blank=True)
    contact      = models.CharField(max_length=20, verbose_name="nomor telepon", blank=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)

    # Make email as username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']

    objects = UserManager() 

    def __str__(self):
        return self.email

    def get_user(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True
