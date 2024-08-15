from typing import Any

from django import forms

from .models import Worker


class ChangeTrackingForm(forms.ModelForm):
    comment = forms.CharField(required=False, max_length=400, widget=forms.Textarea)

    def clean_comment(self) -> Any:
        print('### ins =', self.instance)
        # print('### ins.pk =', getattr(self.instance, 'pk', None))
        # print('### ins.id =', getattr(self.instance, 'id', None))
        # print('### sl.pk =', getattr(self, 'pk', None))
        # print('### sl.id =', getattr(self, 'id', None))
        print('### cd =', self.cleaned_data)
        # print('### cd.pk =', self.cleaned_data.get('pk'))
        # print('### cd.id =', self.cleaned_data.get('id'))
        value = self.cleaned_data.pop('comment', None)
        if self.instance.pk is None:
            return value  # do not save comment when creating a new record

        fields = self.cleaned_data.keys()
        self.is_changed = any((self.cleaned_data[field] != getattr(self.instance, field, None) for field in fields))

        return value


class WorkerForm(ChangeTrackingForm):
    class Meta:
        model = Worker
        fields = 'name', 'phone_number'
