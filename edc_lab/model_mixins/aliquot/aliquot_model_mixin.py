from django.db import models
from django.utils import timezone

from ...choices import (
    ALIQUOT_STATUS, SPECIMEN_MEASURE_UNITS, SPECIMEN_MEDIUM,
    ALIQUOT_CONDITIONS)


class AliquotModelMixin (models.Model):

    aliquot_datetime = models.DateTimeField(
        verbose_name="Date and time aliquot created",
        default=timezone.now)

    is_primary = models.BooleanField(
        default=False,
        editable=False)

    count = models.IntegerField(
        editable=False,
        help_text='pos in sequence of aliquots from parent')

    medium = models.CharField(
        verbose_name='Medium',
        max_length=25,
        choices=SPECIMEN_MEDIUM,
        default='TUBE')

    medium_count = models.IntegerField(
        editable=False,
        default=1,
        help_text='e.g. number of tubes')

    original_measure = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default='5.00')

    current_measure = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default='5.00')

    measure_units = models.CharField(
        max_length=25,
        choices=SPECIMEN_MEASURE_UNITS,
        default='mL')

    status = models.CharField(
        max_length=25,
        choices=ALIQUOT_STATUS,
        default='available')

    condition = models.CharField(
        max_length=25,
        choices=ALIQUOT_CONDITIONS,
        default='10')

    comment = models.CharField(
        max_length=50,
        null=True,
        blank=True)

    def __str__(self):
        return '%s' % (self.aliquot_identifier)

    def natural_key(self):
        return (self.aliquot_identifier,)

    class Meta:
        abstract = True
