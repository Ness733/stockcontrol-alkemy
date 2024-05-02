from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username
