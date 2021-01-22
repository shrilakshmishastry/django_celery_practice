from __future__ import unicode_literals, absolute_import
import sys
from celery import shared_task

from django.core.management import call_command


@shared_task
def bkup():
    sys.stdout = open('db.json', 'w')
    call_command('dumpdata', 'task3')
