from typing import final

from django.db import models


@final
class Qualification(models.Model):
    name = models.CharField("Name", max_length=100, blank=False)
    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.name

