from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            password=password,
            email=email
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("사용자 아이디", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    nickname = models.CharField("닉네임", max_length=50)
    email = models.EmailField("이메일", unique=True)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager() 

    def __str__(self):
        return f"{self.username}입니다."

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin