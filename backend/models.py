from django.db import models
from datetime import timedelta

class Product(models.Model):
    image = models.ImageField(upload_to='uploads/images', default='uploads/images/default.jpg')
    name = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=100, blank=False)
    starting_bid = models.DecimalField(max_digits=6, decimal_places=2)
    bid_start_date = models.DateTimeField(auto_now_add=True)
    auction_duration = models.DurationField(default=timedelta(hours=24))  # Default to 24 hours

    def bid_end_date(self):
        """Calculate auction end time based on bid start date and duration."""
        return self.bid_start_date + self.auction_duration

    def __str__(self):
        return self.name
