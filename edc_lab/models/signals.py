from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from edc_lab.constants import VERIFIED
from edc_lab.models import BoxItem

from .box import Box
from .manifest_item import ManifestItem


@receiver(post_delete, weak=False, sender=ManifestItem,
          dispatch_uid="manifest_item_on_post_delete")
def manifest_item_on_post_delete(sender, instance, using, **kwargs):
    try:
        box = Box.objects.get(box_identifier=instance.identifier)
    except Box.DoesNotExist:
        pass
    else:
        box.status = VERIFIED
        box.save()


@receiver(post_delete, weak=False, sender=BoxItem,
          dispatch_uid="box_item_on_post_delete")
def box_item_on_post_delete(sender, instance, using, **kwargs):
    instance.box.save()
