from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Listings with filtering, search, and ordering.
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["location", "price", "available"]

    search_fields = ["title", "description", "location"]

    ordering_fields = ["price", "created_at"]
    ordering = ["price"]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Bookings with user-specific filtering.
    """

    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Users can only see their own bookings.
        """
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Ensure the booking is tied to the logged-in user.
        """
        serializer.save(user=self.request.user)
