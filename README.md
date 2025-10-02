# Travel App
This project is a Django REST Framework (DRF) API for managing **Listings** and **Bookings** in a travel application.  
It provides **CRUD endpoints** with **filtering, search, ordering**, and **user-specific booking management**.  
API documentation is available via **Swagger** and **Redoc**.

## API Endpoints
### Listings
- `GET /api/listings/` - List all property listings
- `POST /api/listings/` - Create a new listing
- `GET /api/listings/{id}/` - Retrieve a specific listing
- `PUT /api/listings/{id}/` - Update a listing
- `DELETE /api/listings/{id}/` - Delete a listing
  
**Filtering Examples:**
```
GET /api/listings/?location=Paris
GET /api/listings/?price=100
GET /api/listings/?available=true
```
**Search Example:**
```GET /api/listings/?search=beach```

**Ordering Examples:**
```
GET /api/listings/?ordering=price
GET /api/listings/?ordering=-created_at
```
### Bookings
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/{id}/` - Retrieve a specific booking
- `PUT /api/bookings/{id}/` - Update a booking
- `DELETE /api/bookings/{id}/` - Delete a booking
**Example Booking Request (POST):**
```
POST /api/bookings/
Authorization: Token <your_token>
Content-Type: application/json

{
  "listing": 1,
  "check_in": "2025-10-10",
  "check_out": "2025-10-15",
  "guests": 2
}

```
**Response:**
```
{
  "id": 3,
  "user": 1,
  "listing": 1,
  "check_in": "2025-10-10",
  "check_out": "2025-10-15",
  "guests": 2,
  "created_at": "2025-10-01T12:34:56Z"
}
```

### Tests
Use Postman, Swagger UI, or cURL.
Example with cURL:
```
curl -X GET http://127.0.0.1:8000/api/listings/?search=beach```
```
**Example authenticated request:**
```
curl -X GET http://127.0.0.1:8000/api/bookings/ \
     -H "Authorization: Token <your_token>"
```