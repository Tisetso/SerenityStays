from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'available')
    search_fields = ('title', 'location')
    list_filter = ('available', 'location')
