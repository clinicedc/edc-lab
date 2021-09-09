from edc_lab.utils import get_requisition_model_name

LAB = "LAB"
LAB_VIEW = "LAB_VIEW"
LAB_TECHNICIAN_ROLE = "laboratory_technician"

lab_requisition = []
for action in ["view_", "add_", "change_", "delete_", "view_historical"]:
    lab_requisition.append(f".{action}".join(get_requisition_model_name().split(".")))

lab_dashboard_tuples = (
    (
        "edc_dashboard.view_lab_requisition_listboard",
        "Can view Lab requisition listboard",
    ),
    ("edc_dashboard.view_lab_receive_listboard", "Can view Lab receive listboard"),
    ("edc_dashboard.view_lab_process_listboard", "Can view Lab process listboard"),
    ("edc_dashboard.view_lab_pack_listboard", "Can view Lab pack listboard"),
    ("edc_dashboard.view_lab_aliquot_listboard", "Can view Lab aliquot listboard"),
    ("edc_dashboard.view_lab_box_listboard", "Can view Lab box listboard"),
    ("edc_dashboard.view_lab_result_listboard", "Can view Lab result listboard"),
    ("edc_dashboard.view_lab_manifest_listboard", "Can view Lab manifest listboard"),
)

lab_dashboard = [
    "edc_dashboard.view_lab_aliquot_listboard",
    "edc_dashboard.view_lab_box_listboard",
    "edc_dashboard.view_lab_manifest_listboard",
    "edc_dashboard.view_lab_pack_listboard",
    "edc_dashboard.view_lab_process_listboard",
    "edc_dashboard.view_lab_receive_listboard",
    "edc_dashboard.view_lab_requisition_listboard",
    "edc_dashboard.view_lab_result_listboard",
    "edc_dashboard.view_screening_listboard",
    "edc_dashboard.view_subject_listboard",
    "edc_dashboard.view_subject_review_listboard",
]

lab_navbar = [
    "edc_navbar.nav_lab_aliquot",
    "edc_navbar.nav_lab_manifest",
    "edc_navbar.nav_lab_pack",
    "edc_navbar.nav_lab_process",
    "edc_navbar.nav_lab_receive",
    "edc_navbar.nav_lab_requisition",
    "edc_navbar.nav_lab_section",
]

lab = [
    "edc_lab.add_aliquot",
    "edc_lab.add_box",
    "edc_lab.add_boxitem",
    "edc_lab.add_boxtype",
    "edc_lab.add_consignee",
    "edc_lab.add_manifest",
    "edc_lab.add_manifestitem",
    "edc_lab.add_order",
    "edc_lab.add_panel",
    "edc_lab.add_result",
    "edc_lab.add_resultitem",
    "edc_lab.add_shipper",
    "edc_lab.change_aliquot",
    "edc_lab.change_box",
    "edc_lab.change_boxitem",
    "edc_lab.change_boxtype",
    "edc_lab.change_consignee",
    "edc_lab.change_manifest",
    "edc_lab.change_manifestitem",
    "edc_lab.change_order",
    "edc_lab.change_panel",
    "edc_lab.change_result",
    "edc_lab.change_resultitem",
    "edc_lab.change_shipper",
    "edc_lab.delete_aliquot",
    "edc_lab.delete_box",
    "edc_lab.delete_boxitem",
    "edc_lab.delete_boxtype",
    "edc_lab.delete_consignee",
    "edc_lab.delete_manifest",
    "edc_lab.delete_manifestitem",
    "edc_lab.delete_order",
    "edc_lab.delete_panel",
    "edc_lab.delete_result",
    "edc_lab.delete_resultitem",
    "edc_lab.delete_shipper",
    "edc_lab.view_aliquot",
    "edc_lab.view_box",
    "edc_lab.view_boxitem",
    "edc_lab.view_boxtype",
    "edc_lab.view_consignee",
    "edc_lab.view_historicalaliquot",
    "edc_lab.view_historicalbox",
    "edc_lab.view_historicalboxitem",
    "edc_lab.view_historicalconsignee",
    "edc_lab.view_historicalmanifest",
    "edc_lab.view_historicalorder",
    "edc_lab.view_historicalresult",
    "edc_lab.view_historicalresultitem",
    "edc_lab.view_historicalshipper",
    "edc_lab.view_manifest",
    "edc_lab.view_manifestitem",
    "edc_lab.view_order",
    "edc_lab.view_panel",
    "edc_lab.view_result",
    "edc_lab.view_resultitem",
    "edc_lab.view_shipper",
    "edc_navbar.nav_lab_aliquot",
    "edc_navbar.nav_lab_manifest",
    "edc_navbar.nav_lab_pack",
    "edc_navbar.nav_lab_process",
    "edc_navbar.nav_lab_receive",
    "edc_navbar.nav_lab_requisition",
    "edc_navbar.nav_lab_section",
]

lab.extend(lab_requisition)
lab.extend(lab_dashboard)
lab.extend(lab_navbar)


lab_view = [c for c in lab if ("view_" in c or "edc_nav" in c or "edc_dashboard" in c)]
