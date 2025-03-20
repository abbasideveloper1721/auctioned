from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class Product(models.Model):
    image = models.ImageField(upload_to='uploads/images', default='uploads/images/default.jpg')  # Image field
    name = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=100, blank=False)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    bid_start_date = models.DateTimeField(auto_now_add=True)
    auction_duration = models.DurationField(default=timedelta(hours=24))  # Default auction duration of 24 hours

    @property
    def bid_end_date(self):
        """Calculate auction end time."""
        return self.bid_start_date + self.auction_duration

    @property
    def time_left(self):
        """Calculate remaining time for the auction."""
        remaining = self.bid_end_date - now()
        return remaining if remaining.total_seconds() > 0 else timedelta(seconds=0)

    @property
    def status(self):
        """Determine auction status: Active if time remains, otherwise Inactive."""
        return self.time_left.total_seconds() > 0  # True = Active, False = Inactive

    def __str__(self):
        return f"{self.name} ({'Active' if self.status else 'Inactive'})"
