from django.contrib import admin

from edc_base.modeladmin.mixins import (
    ModelAdminRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin, TabularInlineMixin)
from edc_lab.lab_aliquot.admin_mixins import (
    AliquotProcessingModelAdminMixin, AliquotProfileItemModelAdminMixin,
    AliquotProfileModelAdminMixin, AliquotModelAdminMixin, AliquotTypeModelAdminMixin)
from edc_lab.lab_receive.admin_mixins import ReceiveModelAdminMixin
from edc_lab.admin_site import edc_lab_admin

from .models import Receive, Aliquot, AliquotProfileItem, AliquotProfile, AliquotProcessing, AliquotType


class EdcBaseModelAdminMixin(ModelAdminRedirectMixin, ModelAdminFormInstructionsMixin, ModelAdminFormAutoNumberMixin,
                             ModelAdminAuditFieldsMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(Receive, site=edc_lab_admin)
class ReceiveAdmin(ReceiveModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Aliquot, site=edc_lab_admin)
class AliquotAdmin(AliquotModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(AliquotProcessing, site=edc_lab_admin)
class AliquotProcessingAdmin(AliquotProcessingModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(AliquotProfileItem, site=edc_lab_admin)
class AliquotProfileItemAdmin(AliquotProfileItemModelAdminMixin, admin.ModelAdmin):
    pass


class AliquotProfileItemInlineAdmin(TabularInlineMixin, admin.TabularInline):
    model = AliquotProfileItem


@admin.register(AliquotProfile, site=edc_lab_admin)
class AliquotProfileAdmin(AliquotProfileModelAdminMixin, admin.ModelAdmin):
    inlines = [AliquotProfileItemInlineAdmin]


@admin.register(AliquotType, site=edc_lab_admin)
class AliquotTypeAdmin(AliquotTypeModelAdminMixin, admin.ModelAdmin):

    list_display = ('name', 'alpha_code', 'numeric_code')
