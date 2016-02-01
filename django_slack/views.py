from django.http import HttpResponse
from .models import Command

import request

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
            return HttpResponse(result)
        else:
            return HttpResponse(status=401)
    except Command.DoesNotExist as error:
        return HttpResponse(status=404)
    except Exception as error:
        slack_callback(request, error.message)
        return HttpResponse(status=500)
