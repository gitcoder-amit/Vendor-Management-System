from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(
            vendor=vendor,
            status='completed',
            # delivery_date__lte=F('delivery_date')
            delivery_date__lte='2023-12-06'
        )
        breakpoint()
        total_completed_orders = completed_orders.count()
        on_time_deliveries = completed_orders.filter(delivery_date__lte='2023-12-06').count()
        vendor.on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100 if total_completed_orders > 0 else 0
        vendor.save()
