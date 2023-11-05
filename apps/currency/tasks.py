import xml.etree.ElementTree as ET
import requests
from django.db import transaction
from django.utils import timezone

from .models import Currency
from project.celery import app as celery_app


@celery_app.task
def xml_scraping():
    try:
        response = requests.get("https://www.nationalbank.kz/rss/rates_all.xml")
        if response.status_code == 200:
            xml_content = response.content
            data = ET.fromstring(xml_content)
            items = []
            for item_element in data.findall('.//item'):
                title_element = item_element.find('title')
                description_element = item_element.find('description')
                item = {
                    'title': title_element.text if title_element is not None else "N/A",
                    'description': float(description_element.text) if description_element is not None else None,
                }
                items.append(item)
            update_or_create_currency_rates.delay(items)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


@celery_app.task
def update_or_create_currency_rates(items):
    try:
        with transaction.atomic():
            bulk_update_list = []
            for item_data in items:
                currency, created = Currency.objects.get_or_create(
                    name=item_data['title'],
                    rate=item_data['description']
                )

                if not created:
                    currency.rate = item_data['description']
                    currency.updated_at = timezone.now()

                    bulk_update_list.append(currency)

            if bulk_update_list:
                Currency.objects.bulk_update(bulk_update_list, ['rate', 'updated_at'])
            return True
    except Exception as e:
        print(e)
        return False
