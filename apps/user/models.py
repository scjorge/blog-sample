from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = "tb_user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.username)
