from django.db import models


class Currency(models.Model):
    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        db_index=True,
        verbose_name='Currency Name'
    )
    rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Currency rate to KZT'
    )
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True,
        editable=False,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
