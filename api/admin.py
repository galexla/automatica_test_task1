from django.contrib import admin

from .forms import WorkerForm
from .models import Branch, Visit, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    form = WorkerForm


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    search_fields = ['name']


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
