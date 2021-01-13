from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    des = models.TextField()
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    done = models.BooleanField(_("Done"), default=False)

    def __str__(self):
        return self.title