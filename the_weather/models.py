from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=60 , help_text=_('s'))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "شهرها"
        verbose_name = "شهر"
