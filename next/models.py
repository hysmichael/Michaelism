from django.db import models

class NextEntry(models.Model):
    content     = models.TextField()
    created_at  = models.DateField(db_index=True, auto_now_add=True)
    done        = models.BooleanField(default=False)
    username    = models.CharField(max_length=20)
    list_id     = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.content


class NextUser(models.Model):
    username    = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.username

