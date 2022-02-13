from __future__ import absolute_import, unicode_literals
import uuid
from django.conf import settings
from celery import shared_task
import uuid
import requests

uuid = uuid.uuid1()
url_menu = "http://localhost/api/v1/menu/%s" % str(uuid)

@shared_task
def send_slack(options):
    slack_webhook = settings.SLACK_WEBHOOK 

    menu_options = []
    for values in options:
        for key,values in values.items():
            if key == 'description':
                menu_options.append(values)

    payload_descriptions = str(menu_options)
    #payload_descriptions = options
    data_description = "Hola este es el menu de hoy {} {}\n".format(
        url_menu, payload_descriptions)
    dd = {"text":data_description}
    requests.post(slack_webhook, data=str(dd)) 
