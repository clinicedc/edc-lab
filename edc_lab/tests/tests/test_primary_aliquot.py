from django.test import TestCase, override_settings

from edc_lab.identifiers import AliquotIdentifier
from edc_lab.lab import AliquotCreator, AliquotType, PrimaryAliquot


class MyAliquotIdentifier(AliquotIdentifier):
    identifier_length = 16


class MyAliquotCreator(AliquotCreator):
    aliquot_identifier_cls = MyAliquotIdentifier


@override_settings(SITE_ID=10)
class TestPrimaryAliquot(TestCase):
    def test_create_new_primary_aliquot(self):
        aliquot_type = AliquotType(name="aliquot_a", numeric_code="22", alpha_code="WW")
        p = PrimaryAliquot(
            requisition_identifier="ABCDE",
            identifier_prefix="066ABCDE",
            aliquot_type=aliquot_type,
            aliquot_creator_cls=MyAliquotCreator,
        )
        self.assertTrue(p.object)

    def test_get_primary_aliquot(self):
        """Asserts does not recreate aliquot model instance
        if already exists.
        """
        aliquot_type = AliquotType(name="aliquot_a", numeric_code="22", alpha_code="WW")
        p = PrimaryAliquot(
            requisition_identifier="ABCDE",
            identifier_prefix="066ABCDE",
            aliquot_type=aliquot_type,
            aliquot_creator_cls=MyAliquotCreator,
        )
        pk = p.object.id
        aliquot_identifier = p.object.aliquot_identifier
        p = PrimaryAliquot(
            requisition_identifier="ABCDE",
            identifier_prefix="066ABCDE",
            aliquot_type=aliquot_type,
            aliquot_creator_cls=MyAliquotCreator,
        )
        self.assertEqual(aliquot_identifier, p.object.aliquot_identifier)
        self.assertEqual(pk, p.object.id)

    def test_primary_aliquot_exists(self):
        """Asserts primary aliquot exists using identifier_prefix."""
        aliquot_type = AliquotType(name="aliquot_a", numeric_code="22", alpha_code="WW")
        primary_aliquot = PrimaryAliquot(
            requisition_identifier="ABCDE",
            identifier_prefix="066ABCDE",
            aliquot_type=aliquot_type,
            aliquot_creator_cls=MyAliquotCreator,
        )
        obj = primary_aliquot.object
        p = PrimaryAliquot(
            identifier_prefix=obj.identifier_prefix,
            aliquot_creator_cls=MyAliquotCreator,
        )
        self.assertEqual(obj.aliquot_identifier, p.object.aliquot_identifier)

    def test_primary_aliquot_exists2(self):
        """Asserts primary aliquot exists using requisition_identifier."""
        aliquot_type = AliquotType(name="aliquot_a", numeric_code="22", alpha_code="WW")
        primary_aliquot = PrimaryAliquot(
            requisition_identifier="ABCDE",
            identifier_prefix="066ABCDE",
            aliquot_type=aliquot_type,
            aliquot_creator_cls=MyAliquotCreator,
        )
        obj = primary_aliquot.object
        p = PrimaryAliquot(
            requisition_identifier=obj.requisition_identifier,
            aliquot_creator_cls=MyAliquotCreator,
        )
        self.assertEqual(obj.aliquot_identifier, p.object.aliquot_identifier)

    def test_str(self):
        aliquot_type = AliquotType(name="aliquot_a", numeric_code="22", alpha_code="WW")
        primary_aliquot = PrimaryAliquot(
            requisition_identifier="ABCDE",
            identifier_prefix="066ABCDE",
            aliquot_type=aliquot_type,
            aliquot_creator_cls=MyAliquotCreator,
        )
        self.assertTrue(str(primary_aliquot))
