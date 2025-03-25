from rest_framework import serializers
from .models import Product
from datetime import datetime, timezone

class ProductSerializer(serializers.ModelSerializer):
    time_left = serializers.SerializerMethodField()
    
    def get_time_left(self, obj):
        now = datetime.now(timezone.utc)
        if obj.bid_end_date:
            time_diff = obj.bid_end_date - now
            total_seconds = int(time_diff.total_seconds())
            if total_seconds > 0:
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = total_seconds % 60
                return f"{hours}:{minutes:02}:{seconds:02}"
        return "00:00:00"  # Auction ended

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'category', 'starting_bid', 'bid_start_date', 'auction_duration', 'bid_end_date', 'time_left']
