from django.db.models import Model
from django.db.models import TextField
from typing import ClassVar


class Card(Model):
    title = TextField(unique=True)
    content = TextField(blank=True, null=True)  # noqa: DJ001

    class Meta:
        ordering: ClassVar = ["title"]

    def __str__(self) -> str:
        kwargs_list = [f"{f}={getattr(self, f)!r}" for f in ["id", "title"]]
        kwargs = ", ".join(kwargs_list)
        message = f"Card({kwargs})"
        return message
