# edc-lab
Lab classes


###Installation


Get the latest version:

    pip install git+https://github.com/botswana-harvard/edc-lab@develop#egg=edc-lab

Add to settings:

    INSTALLED_APPS = [
        ...
        'edc_lab.apps.AppConfig',
        ...
    ]

    
### Overview

At the facility (e.g. clinic, household + clinic)
specimen collection, label and requisition -> process and label -> pack -> ship

####Step 1: specimen collection, labelling and requisition

`RequisitionModelMixin` and `edc_label`
* Collect the specimen as per protocol (physical)
* The Requisition Crf is completed at the time of specimen collection (data). The Requisition Crf serves to capture if the specimen was (or was not) collected and if so all the details such as volume, condition, date and time;
* Label specimen (physical and data)

The Requisition Crf links the specimen to a processing profile

####Step 2:
 
requisition: filled in with other Crfs, may be more than one requisition model (e.g. maternal, infant)
print labels: print labels for 


###Requisitions

Declare a model or models to store requisition instances. For example:

    class SubjectRequisition(CrfModelMixin, RequisitionModelMixin, RequiresConsentMixin,
                             UpdatesRequisitionMetadataModelMixin, BaseUuidModel):
    
        subject_visit = models.ForeignKey(SubjectVisit)
    
        class Meta:
            app_label = 'edc_example'
            consent_model = 'edc_example.subjectconsent'

The requisition model has a key to the `visit` model so is considered a `Crf` model. But unlike a `crf` model, where each model has one instance per visit, all requisition instances for a subject's visit are instances of the same model with unique `panel names`.

