import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CoreModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)


class UserManager(BaseUserManager):
    def create_user(self, telephone, password):
        if telephone is None:
            raise ValueError('必须输入电话')
        if password is None:
            raise ValueError('必须输入密码')
        user = self.model(telephone=telephone)
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, telephone, password):
        user = self.create_user(telephone=telephone,
                                password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class AbstractUser(AbstractBaseUser, PermissionsMixin, CoreModel):
    """
    抽象用户
    """
    telephone = models.CharField(max_length=11, verbose_name='手机号码', unique=True)
    fullname = models.CharField(max_length=80, blank=True, verbose_name='名称')
    thumbnail = models.ImageField(upload_to="thumbnail", verbose_name='头像', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'telephone'

    def get_short_name(self):
        return self.fullname

    def get_full_name(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        return self.is_admin or perm in self.get_all_permissions()

    def has_module_perms(self, app_label):
        if self.is_admin:
            return True
        else:
            return True

    class Meta:
        abstract = True


class User(AbstractUser):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.telephone

    class Meta:
        permissions = (
            ("view_user", "Can drive"),
        )
        # def Mat
