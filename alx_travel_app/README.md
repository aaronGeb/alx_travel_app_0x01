## Creating Models, Serializers, and Seeders
### Objective

The goal of this project is to define database models, create serializers for API data representation, and implement a management command to seed the database with realistic sample data.


## Models

**In listings/models.py, define the following models:**

**Listing**
- Fields: title, description, price_per_night, location, created_at

**Booking**

- Fields: listing (FK), user (FK), start_date, end_date, status

**Review**

- Fields: listing (FK), user (FK), rating, comment, created_at

Run migrations after defining models:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Serializers

In listings/serializers.py, create serializers:

- ListingSerializer – for the Listing model
- BookingSerializer – for the Booking model

These will handle data representation in API responses.
### Seeder

Create a management command in:
```bash
listings/management/commands/seed.py
```
The command should:

- Insert sample listings, bookings, and reviews into the database.
- Use libraries like faker to generate realistic data.
  
Run the seeder with:
```bash
python manage.py seed listings --number=10
```
### Testing the Seeder
To verify that the database is populated:

**1.Run the Django shell:**
```bash
python manage.py shell
```
**2.Query the database:**
```bash
from listings.models import Listing
print(Listing.objects.all())
```

### Summary

- Models: Listing, Booking, Review

- Serializers: ListingSerializer, BookingSerializer

- Seeder: python manage.py seed listings --number=10

This ensures the database is structured, APIs return serialized data, and the database can be quickly populated for testing.