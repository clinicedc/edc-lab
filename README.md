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

### Usage
Create aliquots and their relationship:
    
    wb = AliquotType(name='whole_blood', alpha_code='WB', numeric_code='02')
    bc = AliquotType(name='buffy_coat', alpha_code='BC', numeric_code='16')
    pl = AliquotType(name='plasmae', alpha_code='PL', numeric_code='32')
    a.add_derivatives(pl, bc)
    
Set up processes:

    processing_profile = ProcessingProfile(
        name='viral_load', aliquot_type=wb)
    process_bc = Process(aliquot_type=bc, aliquot_count=4)
    process_pl = Process(aliquot_type=pl, aliquot_count=2)
    processing_profile.add_processes(process_bc, process_pl)
    
Create a panel(s):

    panel = RequisitionPanel(
        name='panel',
        model=SubjectRequisition,
        aliquot_type=a,
        processing_profile=processing_profile)
    
Create a lab profile:

    lab_profile = LabProfile(
        name='lab_profile',
        requisition_model=SubjectRequisition)
    lab_profile.add_panel(panel)
    
Register the `lab_profile` with site:

    site_labs.register(lab_profile)
