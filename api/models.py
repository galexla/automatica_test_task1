from auditlog.models import LogEntry
from auditlog.registry import auditlog
from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    # is_authenticated() - метод для проверки аутентификации
    @staticmethod
    def is_authenticated():
        return True


class Branch(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Visit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()


class ChangeTrackingComment(models.Model):
    log_entry = models.OneToOneField(LogEntry, related_name='comment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
