import uuid

from django.conf import settings

from celery import shared_task
import uuid
from backend_test.celery import app
from secret import TOKEN_SLACK
from slackclient import SlackClient

uuid = uuid.uuid1()
url_menu = "http://localhost/api/v1/menu/%s" % str(uuid)


@shared_task
def send_slack(options):
    token = settings.SLACK_TOKEN
    sc = SlackClient(slack_token)

    menu_options = []
    for o in option:
        menu_options.append(str(o.description))

    descriptions = str(menu_options)

    sc.api_call(
        "chat.postMessage",
        channel=settings.SLACK_CHANNEL,
        text="Hola!. \n  este es el menu de hoy\n"+ descriptions + "\nurl : "+ url_menu +" \n Excelente día ! "
    )
