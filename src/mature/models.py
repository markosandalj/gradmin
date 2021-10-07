from django.db import models
from datetime import datetime
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from skripte.models import Subject

# MATURA related models
class Year(models.Model):
    available_years = [(x, str(x)) for x in range(2010, datetime.now().year+1)]
    year = models.IntegerField(choices=available_years, unique=True,)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        ordering = ['-year']

    def __str__(self):
        return str(self.year)

class Term(models.Model):

    class TermChoices(models.TextChoices):
        LJETO = 'ljeto', _('Ljetni rok')
        JESEN = 'jesen', _('Jesenski rok')
        ZIMA = 'zima', _('Zimski rok')

    term = models.CharField(
        max_length=5,
        choices=TermChoices.choices,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.term)

class MaturaSubject(models.Model):
    class MaturaLevels(models.TextChoices):
        A_RAZINA = "A", _('Viša razina')
        B_RAZINA = "B", _('Niža razina')
        NEMA_RAZINE = 0, _('Nema razine')

    level = models.CharField(
        max_length=2,
        choices=MaturaLevels.choices,
        default=MaturaLevels.NEMA_RAZINE,
    )
    subject = ForeignKey(
        Subject,
        blank=True,
        null=True,
        on_delete=SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return str(self.subject.name + ' ' + self.level)


class Matura(models.Model):
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    term = models.ForeignKey(Term, on_delete=models.PROTECT)
    subject = models.ForeignKey(MaturaSubject, on_delete=models.PROTECT, blank=True, null=True,)
    vimeo_folder_id = models.BigIntegerField(blank=True, null=True,)
    shopify_product_id = models.BigIntegerField(blank=True, null=True,)
    shopify_product_url = models.URLField(blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        ordering = ['year',]

    def __str__(self):
        razina = self.subject.level if self.subject.level != self.subject.MaturaLevels.NEMA_RAZINE else ''
        return f'DM {str(self.subject.subject.name)} {razina} {str(self.year)} {str(self.term)}'
        