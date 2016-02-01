from django.db import models
from django.utils.translation import ugettext_lazy as _


class Command(models.Model):
    command = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    code = models.TextField()
    is_enabled = models.BooleanField(default=False)
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name=_('dt_created'))
    dt_updated = models.DateTimeField(auto_now=True, verbose_name=_('dt_updated'))

    class Meta:
        app_label = 'django_slack'
        verbose_name = 'Slack Comment'
        verbose_name_plural = 'Slack Comments'
        get_latest_by = 'id'

    def __unicode__(self):
        return '%s' % (self.command,)

