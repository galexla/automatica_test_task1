from typing import Any, List, Optional, Tuple

from auditlog.models import LogEntry
from auditlog.signals import post_log
from django.dispatch import Signal, receiver
from rest_framework.request import Request

from .models import ChangeTrackingComment


@receiver(post_log)
def set_order_owner_by_basket_id(
    sender,
    instance,
    action: LogEntry.Action,
    changes: Optional[dict],
    log_entry: Optional[LogEntry],
    log_created: bool,
    error: Optional[Exception],
    pre_log_results: List[Tuple[Any, Any]],
    **kwargs,
) -> None:
    if action == LogEntry.Action.UPDATE:
        print('### sender =', sender)
        print('### instance =', instance.__dict__)
        print('### changes =', changes)
        print('### log_entry =', log_entry.__dict__)
        print('### log_created =', log_created)
        print('### error =', error)
        print('### pre_log_results =', pre_log_results)
        comment = ChangeTrackingComment()
        comment.log_entry = log_entry
        comment.save()
