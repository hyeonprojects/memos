from datetime import datetime, timezone

from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'email: {} & name : {}'.format(self.email, self.name)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.now(timezone.utc)
        self.save()

    class Meta:
        db_table = 'user'
        ordering = ['-created_at']
