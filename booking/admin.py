from django.contrib import admin
from .models import BookMix


@admin.register(BookMix)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "time",
        "stems",
        "price",
    )
