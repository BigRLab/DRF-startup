import time
from celery import task


@task()
def adds(x, y):
    time.sleep(3)
    return x + y
