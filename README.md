# edc-lab
Lab classes


from edc_lab.aliquot.model_mixins import AliquotModelMixin
from edc_lab.specimen.model_mixins import SpecimenCollectionModelMixin, SpecimenCollectionItemModelMixin


Declare a model to store requisition instances. For example:

    class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                             UpdatesRequisitionMetadataModelMixin, BaseUuidModel):
    
        subject_visit = models.ForeignKey(SubjectVisit)
    
        class Meta:
            app_label = 'edc_example'
            consent_model = 'edc_example.subjectconsent'

The requisition model has a key to the `visit` model so is considered a `Crf` model. But unlike a `crf` model, where each model has one instance per visit, all requisition instances for a subject's visit are instances of the same model with unique `panel names`.
    
Declare a panel model:

    class Panel(BaseUuidModel):
    
        name = models.CharField(max_length=25)
    
        class Meta:
            app_label = 'edc_example'


    class Aliquot(AliquotModelMixin, BaseUuidModel):

        class Meta(AliquotModelMixin.Meta):
        
            app_label = 'edc_example'


    class SpecimenCollection(SpecimenCollectionModelMixin, BaseUuidModel):
    
        class Meta(SpecimenCollectionModelMixin.Meta):
            app_label = 'edc_example'
    
    
    class SpecimenCollectionItem(SpecimenCollectionItemModelMixin, BaseUuidModel):
    
        specimen_collection = models.ForeignKey(SpecimenCollection)
    
        class Meta(SpecimenCollectionItemModelMixin.Meta):
            app_label = 'edc_example'
    
    
            