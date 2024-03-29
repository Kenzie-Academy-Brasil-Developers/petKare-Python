from django.db import models


class Trait(models.Model):

    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<{[self.id]} {self.name}>"  # type: ignore
