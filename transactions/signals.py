from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from .models import Purchase
from django.db import transaction

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Purchase)
def update_item_quantity(sender, instance, **kwargs):
    """
    Updates the item quantity only if the delivery status is "Successful"
    and the quantity has not been updated before.
    """
    if instance.delivery_status == "S" and not instance.quantity_updated:
        try:
            with transaction.atomic():
                item = instance.item
                item.quantity += instance.quantity
                item.save()
                instance.quantity_updated = True  # Mark quantity as updated
                instance.save(update_fields=["quantity_updated"])  # Save only this field
                logger.info(f"Updated quantity for item: {item.name} by {instance.quantity}")
        except Exception as e:
            logger.error(f"Failed to update item quantity: {e}")
    else:
        logger.warning(
            f"Delivery status is not 'Successful' or quantity already updated. "
            f"No changes made for item: {instance.item.name}"
        )
