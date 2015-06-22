from django.db import models
from django.db.models import permalink

class Essay(models.Model):
    title       = models.CharField(max_length=100, unique=True)
    slug        = models.SlugField(max_length=100, unique=True)
    preface     = models.TextField(null=True, blank = True)
    body        = models.TextField()
    created_at  = models.DateField(db_index=True, auto_now_add=True)
    posted_at   = models.DateField(db_index=True, null=True, blank=True)
    tags        = models.ManyToManyField('Tag', related_name='essays', blank=True)
    bundle      = models.ForeignKey('EssayBundle', related_name='essays', null=True, blank=True)
    language    = models.ForeignKey('Language', related_name='essays')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('ideas-single-essay', None, { 'slug': self.slug })

    def all_tags(self):
        string = ''
        if not self.tags.exists():
            return u'(None)'
        return ', '.join(['%s' % tag.name for tag in self.tags.all()])


class Tag(models.Model):
    name        = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.name


class EssayBundle(models.Model):
    def __unicode__(self):
        essays = self.essays.all()
        if len(essays) == 0:
            return '(New) %s' % self.pk
        representative_title = essays[0].title
        return '%s (%d)' % (representative_title, len(essays))


class Language(models.Model):
    name            = models.CharField(max_length=20, db_index=True)
    localized_name  = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.name

    def full_name(self):
        if self.name == self.localized_name:
            return self.name
        return '%s (%s)' % (self.name, self.localized_name)

