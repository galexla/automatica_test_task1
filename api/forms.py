from typing import Any

from auditlog.models import LogEntry
from django import forms

from .models import Branch, ChangeTrackingComment, Worker


class ChangeTrackingForm(forms.ModelForm):
    comment = forms.CharField(required=False, max_length=400, widget=forms.Textarea)

    def clean_comment(self) -> Any:
        value = self.cleaned_data.pop('comment', None)

        if self.instance.pk is None:
            return value  # не сохранять комментарий, когда создается новая запись

        changes = self.get_changes(self.cleaned_data)
        if changes and not value:
            raise forms.ValidationError('Пожалуйста, напишите, почему вы вносите эти изменения.')

        if changes:
            log_entry = LogEntry.objects.log_create(self.instance, action=LogEntry.Action.UPDATE, changes=changes)
            comment = ChangeTrackingComment()
            comment.comment = value
            comment.log_entry = log_entry
            comment.save()

        return value

    def get_changes(self, cleaned_data: dict) -> str:
        changes = {}
        fields = list(cleaned_data.keys())
        for field in fields:
            old_value = getattr(self.instance, field, None)
            new_value = cleaned_data.get(field)
            if new_value != old_value:
                changes[field] = [old_value, new_value]
        return changes or None


class WorkerForm(ChangeTrackingForm):
    class Meta:
        model = Worker
        fields = 'name', 'phone_number'


class BranchForm(ChangeTrackingForm):
    class Meta:
        model = Branch
        fields = 'name', 'worker'
