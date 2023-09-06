import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from testingMaptemplate.models import FoodmapStore


class Command(BaseCommand):
    help = 'Load data from Foodmap store file'

    def handle(self, *args, **options):
        data_file = settings.BASE_DIR / 'mapdatarecord' / 'foodmap_info_half_done_two.csv'
        keys = ('district', 'restaurantName', 'address', 'contactInfo', 'googlereviewlink', 'openingtime', 'latitude',
                'longitude', 'ratingintotaloffive', 'ratingcategories')  # the CSV columns we will gather data from.

        records = []
        with open(data_file, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        # extract the latitude and longitude from the Point object
        # longitude = record['longitude'] = float(longitude)
        # latitude = record['latitude'] = float(latitude)

        # add the data to the database
        for record in records:
            FoodmapStore.objects.get_or_create(
                district=record['district'],
                restaurantname=record['restaurantName'],
                address=record['address'],
                contactinfo=record['contactInfo'],
                googlelink=record['googlereviewlink'],
                openingtime=record['openingtime'],
                latitude=record['latitude'],
                longitude=record['longitude'],
                ratingintotaloffive=record['ratingintotaloffive'],
                ratingcategories=record['ratingcategories'],
            )
