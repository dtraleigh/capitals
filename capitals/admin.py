from django.contrib import admin
from capitals.models import Photo, Capital

class photo_admin(admin.ModelAdmin):
    list_display = ('name', 'photo_file')

class capital_admin(admin.ModelAdmin):
    list_display = ('name', 'us_state', 'date_visited', 'lat', 'lon')

admin.site.register(Photo, photo_admin)
admin.site.register(Capital, capital_admin)
