from django.db import models

from .fields import CurrentUserField


class AbstractModel(models.Model):
    """
    Base model for any type of model with default fields
    """

    created_by = CurrentUserField(related_name="%(app_label)s_%(class)s_created_by")
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_by = CurrentUserField(on_update=True, related_name="%(app_label)s_%(class)s_updated_by")
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.pk}>"

    class Meta:
        abstract = True
