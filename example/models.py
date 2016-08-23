from django.apps import apps as django_apps
from django.db import models
from django.core.urlresolvers import reverse
from simple_history.models import HistoricalRecords

from edc_base.model.models import BaseUuidModel
from edc_lab.lab_aliquot.managers import (
    AliquotConditionManager, AliquotManager, AliquotProfileManager,
    AliquotProfileItemManager, AliquotTypeManager, AliquotProcessingManager)
from edc_lab.lab_receive.model_mixins import ReceiveModelMixin
from edc_lab.lab_receive.managers import ReceiveManager
from edc_lab.lab_aliquot.model_mixins import (
    AliquotProfileItemModelMixin, AliquotProfileModelMixin,
    AliquotProcessingModelMixin, AliquotConditionModelMixin, AliquotModelMixin,
    AliquotTypeModelMixin)
from edc_registration.mixins import RegisteredSubjectMixin

# from lab_requisition.models import RequisitionModelMixin


class Receive(ReceiveModelMixin, BaseUuidModel):

    objects = ReceiveManager()

    history = HistoricalRecords()

    def requisition(self):
        url = reverse('edc_lab_admin:{}_changelist'.format(self.requisition_model_name.replace('.', '_')))
        return '<a href="{0}?q={1}">{1}</a>'.format(url, self.requisition_identifier)
    requisition.allow_tags = True

    class Meta:
        app_label = 'example'


class AliquotCondition(AliquotConditionModelMixin):

    objects = AliquotConditionManager()

    class Meta:
        app_label = 'example'


class AliquotType(AliquotTypeModelMixin, BaseUuidModel):

    objects = AliquotTypeManager()

    class Meta:
        app_label = 'example'
        ordering = ["name"]


class Aliquot(AliquotModelMixin, RegisteredSubjectMixin, BaseUuidModel):

    receive = models.ForeignKey(
        Receive,
        editable=False)

    aliquot_type = models.ForeignKey(
        AliquotType,
        verbose_name="Aliquot Type",
        null=True)

    aliquot_condition = models.ForeignKey(
        AliquotCondition,
        verbose_name="Aliquot Condition",
        null=True,
        blank=True)

    objects = AliquotManager()

    history = HistoricalRecords()

    @property
    def specimen_identifier(self):
        return self.aliquot_identifier[:-4]

    @property
    def aliquot_count(self):
        return int(self.aliquot_identifier[-2:])

    @property
    def registered_subject(self):
        return self.receive.registered_subject

    @property
    def requisition(self):
        model_name = self.receive.requisition_model_name
        model = django_apps.get_model(self._meta.app_label, model_name)
        return model.objects.get(requisition_identifier=self.receive.requisition_identifier)

    @property
    def visit_code(self):
        return self.receive.visit

    def processing(self):
        app_config = django_apps.get_app_config('edc_lab')
        url = reverse('edc_lab_admin:{app_label}_aliquotprocessing_add'.format(app_config.app_label))
        return '<a href="{0}?aliquot={1}">process</a>'.format(url, self.pk)
    processing.allow_tags = True

    class Meta:
        app_label = 'example'
        unique_together = (('receive', 'count'), )


class AliquotProfile(AliquotProfileModelMixin, BaseUuidModel):

    aliquot_type = models.ForeignKey(
        AliquotType,
        verbose_name='Source aliquot type')

    objects = AliquotProfileManager()

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        app_label = 'example'


class AliquotProfileItem(AliquotProfileItemModelMixin, BaseUuidModel):

    profile = models.ForeignKey(AliquotProfile)

    aliquot_type = models.ForeignKey(AliquotType)

    objects = AliquotProfileItemManager()

    def __str__(self):
        return str(self.aliquot_type)

    def natural_key(self):
        return self.profile.natural_key() + self.aliquot_type.natural_key()

    class Meta:
        app_label = 'example'
        unique_together = ('profile', 'aliquot_type')


class AliquotProcessing(AliquotProcessingModelMixin, BaseUuidModel):

    aliquot = models.ForeignKey(
        Aliquot,
        verbose_name='Source Aliquot',
        help_text='Create aliquots from this one.')

    profile = models.ForeignKey(
        AliquotProfile,
        verbose_name='Profile',
        help_text='Create aliquots according to this profile.')

    objects = AliquotProcessingManager()

    history = HistoricalRecords()

    def natural_key(self):
        return self.aliquot.natural_key() + self.profile.natural_key()

    def deserialize_get_missing_fk(self, attrname):
        retval = None
        return retval

    class Meta:
        app_label = 'example'


# class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, BaseUuidModel):
# 
#     aliquot_model = Aliquot
# 
#     maternal_visit = models.ForeignKey(MaternalVisit)
# 
#     packing_list = models.ForeignKey(PackingList, null=True, blank=True)
# 
#     aliquot_type = models.ForeignKey(AliquotType)
# 
#     panel = models.ForeignKey(Panel)
# 
#     # objects = MaternalRequisitionManager()
# 
#     history = HistoricalRecords()
# 
#     # entry_meta_data_manager = RequisitionMetaDataManager(MaternalVisit)
# 
#     def __str__(self):
#         return '{0} {1}'.format(str(self.panel), self.requisition_identifier)
# 
#     def natural_key(self):
#         return (self.requisition_identifier,)
# 
#     class Meta:
#         app_label = 'td_lab'
#         verbose_name = 'Maternal Requisition'
#         verbose_name_plural = 'Maternal Requisition'
#         unique_together = ('maternal_visit', 'panel', 'is_drawn')
#         ordering = ('-created', )
