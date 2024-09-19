from django.db import models
from django.utils import timezone
from typing import Dict, Any


class NumberRequest(models.Model):
    number: int = models.PositiveIntegerField(db_index=True)
    occurrences: int = models.PositiveIntegerField(default=1)
    last_datetime: models.DateTimeField = models.DateTimeField(auto_now=True)
    value: int = models.PositiveIntegerField(null=False)

    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.pk is not None:
            original: NumberRequest = NumberRequest.objects.get(pk=self.pk)

            if original.number == self.number:
                self.occurrences = original.occurrences + 1

        super().save(*args, **kwargs)

    def increment(self) -> None:
        self.occurrences += 1
        self.last_datetime = timezone.now()

    def to_json(self) -> Dict[str, Any]:
        return {
            "datetime": timezone.now(),
            "value": self.value,
            "number": self.number,
            "occurrences": self.occurrences,
            "last_datetime": self.last_datetime,
        }

    def __str__(self) -> str:
        return f"Number {self.number} - Value {self.value}"
