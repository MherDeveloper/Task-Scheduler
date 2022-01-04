from django.db import models


class Event(models.Model):
    datetime = models.DateTimeField('datetime')

    def __str__(self):
        return str(self.datetime)