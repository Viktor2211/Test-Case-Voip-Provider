from django.db import models


class CDR(models.Model):

    class Statuses(models.TextChoices):
        SUCCESSFULL = 's', 'Успешный'
        REJECTED = 'r', 'Отклоненный'
        MISSED = 'm', 'Пропущенный'

    class CallType(models.TextChoices):
        OUTGOING_CALL = 'o', 'Исходящий'
        INCOMING_CALL = 'i', 'Входящий'
        MISSED_CALL = 'm', 'Пропущенный'

    called_number = models.CharField(max_length=15)
    calling_number = models.CharField(max_length=15)
    call_start_time = models.DateTimeField()
    call_end_time = models.DateTimeField()
    call_duration = models.IntegerField()
    status = models.CharField(
        max_length=1, choices=Statuses.choices, default=Statuses.SUCCESSFULL)
    call_type = models.CharField(max_length=1, choices=CallType.choices, default=CallType.INCOMING_CALL)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_call_type_display(self):
        return dict(CDR.CallType.choices)[self.call_type]
