from django.db import models
from django.utils.translation import ugettext_lazy as _


class Command(models.Model):
    command = models.CharField(max_length=32, verbose_name='command')
    description = models.CharField(max_length=256, verbose_name='description')
    code = models.TextField(verbose_name='code')
    is_enabled = models.BooleanField(default=False, verbose_name='is_enabled')
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name=_('dt_created'))
    dt_updated = models.DateTimeField(auto_now=True, verbose_name=_('dt_updated'))

    class Meta:
        app_label = 'django_slack'
        verbose_name = _('Slack Comment')
        verbose_name_plural = _('Slack Comments')
        get_latest_by = 'id'

    def __unicode__(self):
        return '%s' % (self.command,)

class CommandLog(models.Model):
    team_id = models.CharField(max_length=64, verbose_name=_('team_id'))
    team_domain = models.CharField(max_length=256, verbose_name=_('team_domain'))
    channel_id = models.CharField(max_lenggth=256, verbose_name=_('channel_id'))
    user_id = models.CharField(max_length=64, verbose_name=_('user_id'))
    user_name = models.CharField(max_length=64, verbose_name=_('user_name'))
    command = models.CharField(max_length=64, verbose_name=_('command'))
    text = models.TextField(default='', verbose_name=_('text'))
    response_url = models(max_length=256, verbose_name=_('response_url'))
    request_payload = models.TextField(default='', verbose_name=_('request_payload'))
    response_payload = models.TextField(default='', verbose_name=_('response_payload'))
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name=_('dt_created'))

    class Meta:
        app_label = 'django_slack'
        verbose_name = _('Slack Command Log')
        verbose_name_plural = _('Slack Command Logs')
        get_latest_by = 'id'

    def __unicode__(self):
        return '%s %s' % (self.id, self.user_name)
