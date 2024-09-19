from django.db import models
from django.utils import timezone


class NumberRequest(models.Model):
    number = models.PositiveIntegerField(db_index=True)
    occurrences = models.PositiveIntegerField(default=1)
    last_datetime = models.DateTimeField(auto_now=True)
    value = models.PositiveIntegerField(null=False)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = NumberRequest.objects.get(pk=self.pk)

            if original.number == self.number:
                self.occurrences = original.occurrences + 1

        super().save(*args, **kwargs)

    def increment(self):
        self.occurrences += 1
        self.last_datetime = timezone.now()
        self.save()

    def to_json(self):
        return {
            "datetime": timezone.now(),
            "value": self.value,
            "number": self.number,
            "occurrences": self.occurrences,
            "last_datetime": self.last_datetime,
        }

    def __str__(self):
        return f"Number {self.number} - Value {self.value}"
