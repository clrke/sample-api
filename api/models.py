from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def serialize(self):
        return {
                'id': self.id,
                'author': self.author,
                'content': self.content,
                'created': self.created,
                'updated': self.updated
            }

