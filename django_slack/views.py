from django.http import HttpResponse
from .models import Command
from .models import CommandLog

import requests

def make_log(request, response):
    if request.method == 'POST':
        team_id = request.POST.get('team_id')
        team_domain = request.POST.get('team_domain')
        channel_id = request.POST.get('channel_id')
        channel_name = request.POST.get('channel_name')
        user_id = request.POST.get('user_id')
        user_name = request.POST.get('user_name')
        command = request.POST.get('command')
        text = request.POST.get('text')
        response_url = request.POST.get('response_url')
        response_payload = response.content
        CommandLog.objects.create(
                team_id=team_id,
                team_domain=team_domain,
                channel_id=channel_id,
                channel_name=channel_name,
                user_id=user_id,
                user_name=user_name,
                command=command,
                text=text,
                response_url=response_url,
                response_payload=response_payload,
                )



def slack_callback(request, text):
    if request.POST.get('response_url'):
        res = requests.post(
                url=request.POST.get('response_url'),
                data={'text': text},
                headers={
                    'content-type': 'application/json',
                    }
                )


def slack_cli(request, command):
    try:
        command_obj = Command.objects.get(command=command)
        if command_obj.is_enabled:
            command_dict = {}
            exec command_obj.code in command_dict
            command_func = command_dict.get('command_func') or (lambda *args, **kwargs: None)
            result = command_func(request)
            slack_callback(request, result)
            response =  HttpResponse(result)
        else:
            response =  HttpResponse(status=401)
    except Command.DoesNotExist as error:
        response =  HttpResponse(status=404)
    except Exception as error:
        slack_callback(request, error.message)
        response =  HttpResponse(status=500)
    make_log(request, response)
    return response
