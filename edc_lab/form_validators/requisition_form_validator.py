from django import forms
from django.apps import apps as django_apps
from edc_constants.constants import NO, YES
from edc_crf.crf_form_validator import CrfFormValidator
from edc_utils import formatted_datetime, to_utc

from ..form_validators import CrfRequisitionFormValidatorMixin


class RequisitionFormValidator(CrfRequisitionFormValidatorMixin, CrfFormValidator):

    aliquot_model = "edc_lab.aliquot"

    @property
    def aliqout_model_cls(self):
        return django_apps.get_model(self.aliquot_model)

    def clean(self) -> None:
        if self.instance:
            if self.cleaned_data.get("packed") != self.instance.packed:
                raise forms.ValidationError({"packed": "Value may not be changed here."})
            elif self.cleaned_data.get("processed") != self.instance.processed:
                if self.aliqout_model_cls.objects.filter(
                    requisition_identifier=self.instance.requisition_identifier
                ).exists():
                    raise forms.ValidationError(
                        {"processed": "Value may not be changed. Aliquots exist."}
                    )
            elif not self.cleaned_data.get("received") and self.instance.received:
                if self.instance.processed:
                    raise forms.ValidationError(
                        {"received": "Specimen has already been processed."}
                    )
            elif self.cleaned_data.get("received") and not self.instance.received:
                raise forms.ValidationError(
                    {"received": "Receive specimens in the lab section of the EDC."}
                )
            elif self.instance.received:
                raise forms.ValidationError(
                    "Requisition may not be changed. The specimen has "
                    "already been received."
                )

        self.validate_requisition_datetime()
        self.applicable_if(NO, field="is_drawn", field_applicable="reason_not_drawn")
        self.validate_other_specify(field="reason_not_drawn")
        self.required_if(YES, field="is_drawn", field_required="drawn_datetime")
        self.validate_drawn_datetime()
        self.applicable_if(YES, field="is_drawn", field_applicable="item_type")
        self.required_if(YES, field="is_drawn", field_required="item_count")
        self.required_if(YES, field="is_drawn", field_required="estimated_volume")

    @staticmethod
    def validate_assay_datetime(assay_datetime, requisition, field) -> None:
        if assay_datetime:
            assay_datetime = to_utc(assay_datetime)
            requisition_datetime = to_utc(requisition.requisition_datetime)
            if assay_datetime < requisition_datetime:
                raise forms.ValidationError(
                    {
                        field: (
                            f"Invalid. Cannot be before date of requisition "
                            f"{formatted_datetime(requisition_datetime)}."
                        )
                    }
                )

    def validate_requisition_datetime(self) -> None:
        requisition_datetime = self.cleaned_data.get("requisition_datetime")
        subject_visit = self.cleaned_data.get("subject_visit")
        if requisition_datetime:
            report_datetime = to_utc(subject_visit.report_datetime)
            requisition_datetime = to_utc(requisition_datetime)
            if requisition_datetime < report_datetime:
                raise forms.ValidationError(
                    {
                        "requisition_datetime": f"Invalid. Cannot be before date of visit "
                        f"{formatted_datetime(report_datetime)}."
                    }
                )

    def validate_drawn_datetime(self):
        if (
            self.cleaned_data.get("requisition_datetime")
            and self.cleaned_data.get("drawn_datetime")
            and self.cleaned_data.get("drawn_datetime").date()
            > self.cleaned_data.get("requisition_datetime").date()
        ):
            raise forms.ValidationError(
                {"drawn_datetime": "Invalid. Cannot be after requisition date."}
            )

        related_visit = self.cleaned_data.get(self.instance.related_visit_model_attr())
        if (
            self.cleaned_data.get("drawn_datetime")
            and self.cleaned_data.get("drawn_datetime").date()
            < related_visit.report_datetime.date()
        ):
            raise forms.ValidationError(
                {"drawn_datetime": "Invalid. Cannot be before the visit date."}
            )
