from celery import shared_task

@shared_task
def cleanup():
    print('clean up the Trash')


