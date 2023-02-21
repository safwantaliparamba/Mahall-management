import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser,Group


PROFILE_TYPES = (
    ("chief","Chief"),
    ("user","User")
)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    is_deleted = models.BooleanField(default=False)
    profile_type = models.CharField(max_length=128,choices=PROFILE_TYPES,default="user")
    # is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('date_joined',)

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.profile_type == "chief":
                group,created = Group.objects.get_or_create(name="chief")
                self.groups.add(group)

        super(User, self).save(*args, **kwargs)