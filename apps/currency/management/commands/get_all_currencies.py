from django.core.management.base import BaseCommand

from apps.currency.models import Currency


class Command(BaseCommand):
    help = 'Get data about all currencies'

    def handle(self, *args, **options):
        currencies = Currency.objects.all()

        if currencies.exists():
            self.stdout.write("Currency ID | Currency Name | Rate to KZT | Created At | Updated At")
            self.stdout.write("-" * 70)

            for currency in currencies:
                self.stdout.write(f"{currency.id} | {currency.name} | "
                                  f"{currency.rate} | {currency.created_at} | "
                                  f"{currency.updated_at}")

            self.stdout.write("-" * 70)
        else:
            self.stdout.write("No currencies found in the database.")