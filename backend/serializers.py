from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    bid_end_date = serializers.SerializerMethodField()
    time_left = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)  # Ensure image URL is returned

    def get_bid_end_date(self, obj):
        return obj.bid_end_date

    def get_time_left(self, obj):
        return str(obj.time_left)  # Converts timedelta to a readable format like "23:59:10"

    def get_status(self, obj):
        return "Active" if obj.status else "Inactive"  # Returns a human-readable status

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'category', 'starting_bid', 'bid_start_date', 'auction_duration', 'bid_end_date', 'time_left', 'status']
