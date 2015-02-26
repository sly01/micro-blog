from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User)
    #owner = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '%s - %s' % (self.user, self.title)