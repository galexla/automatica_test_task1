from auditlog.admin import LogEntryAdmin
from auditlog.models import LogEntry
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .forms import BranchForm, WorkerForm
from .models import Branch, Visit, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    form = WorkerForm


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    search_fields = ['name']
    form = BranchForm


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ['worker__name', 'branch__name']
    list_display = ['datetime', 'worker', 'branch']

    # Запретить редактирование
    def has_change_permission(self, request, obj=None):
        return False

    # Переопределение прав доступа для удаления
    def has_delete_permission(self, request, obj=None):
        return False  # Запретить удаление


class CustomLogEntryAdmin(LogEntryAdmin):
    list_display = [
        'created',
        'resource_url',
        'action',
        'msg_short',
        'user_url',
        'cid_url',
        'get_comment',
    ]
    readonly_fields = ['created', 'resource_url', 'action', 'user_url', 'msg', 'get_comment']
    fieldsets = [
        (None, {'fields': ['created', 'user_url', 'resource_url', 'cid', 'get_comment']}),
        (_('Changes'), {'fields': ['action', 'msg']}),
    ]

    def get_comment(self, obj):
        return obj.comment.comment if hasattr(obj, 'comment') else 'No Comment'

    get_comment.short_description = 'Comment'


admin.site.unregister(LogEntry)
admin.site.register(LogEntry, CustomLogEntryAdmin)
