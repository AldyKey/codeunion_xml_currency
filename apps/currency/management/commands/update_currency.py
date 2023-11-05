from django.core.management.base import BaseCommand

from apps.currency.models import Currency


class Command(BaseCommand):
    help = 'Update currency rate by ID'

    def handle(self, *args, **options):
        try:
            currency_id = int(input("Enter the currency ID: "))
            new_rate = float(input("Enter the new rate: "))

            currency = Currency.objects.get(pk=currency_id)
            currency.rate = new_rate
            currency.save()
            self.stdout.write(f'Successfully updated currency (ID: {currency_id}) rate to {new_rate}')
        except Currency.DoesNotExist:
            self.stderr.write(f'Currency with ID {currency_id} does not exist.')
        except Exception as e:
            self.stderr.write(f'An error occurred: {str(e)}')
