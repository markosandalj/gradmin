from pyexpat import model
from django.db import models

# Create your models here.

class Cheatsheet(models.Model):
    name = models.TextField(blank=False, null=False)
    subject = models.ForeignKey("skripte.Subject", null=True, blank=True, on_delete=models.SET_NULL)
    layout = models.ForeignKey('CheatsheetLayout', null=True, blank=True, on_delete=models.SET_NULL)
    file = models.ForeignKey('media.PDF', null = True, blank = True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)

class CheatsheetSection(models.Model):
    name = models.TextField(blank=False, null=False)
    decorator = models.TextField(blank=True, null=True)
    cheatsheet = models.ForeignKey('Cheatsheet', on_delete=models.CASCADE)
    section_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('section_order',)

    def __str__(self):
        return str(self.name + ' ' + self.decorator)

class CheatsheetTable(models.Model):
    name = models.TextField(blank=False, null=False, default='Konstante')
    decorator = models.TextField(blank=True, null=True)
    cheatsheet = models.ForeignKey('Cheatsheet', on_delete=models.CASCADE)
    table_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('table_order',)

    def __str__(self):
        return str(self.name)


class CheatsheetSeactionEquation(models.Model):
    cheatsheet_section = models.ForeignKey('CheatsheetSection', on_delete=models.PROTECT)
    equation = models.ForeignKey('skripte.Equation', on_delete=models.PROTECT)
    equation_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('equation_order',)

class CheatsheetTableEquation(models.Model):
    cheatsheet_table = models.ForeignKey('CheatsheetTable', on_delete=models.PROTECT)
    equation = models.ForeignKey('skripte.Equation', on_delete=models.PROTECT)
    equation_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('equation_order',)


class CheatsheetLayout(models.Model):
    name = models.TextField(blank=False, null=False)
    css_class = models.TextField(blank=False, null=False)

    def __str__(self):
        return str(self.name)