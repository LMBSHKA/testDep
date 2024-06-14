from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    about = models.CharField(max_length= 300, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    cat = models.ForeignKey('Upload_images', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class Upload_images(models.Model):
    user_id = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="images")
    category = models.CharField(max_length=256, null=True, blank=True)