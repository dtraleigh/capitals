from django.contrib import admin
from capitals.models import Photo, Capital, Country

class photo_admin(admin.ModelAdmin):
    list_display = ('name', 'photo_file', 'photo_width', 'photo_height')

class capital_admin(admin.ModelAdmin):
    list_display = ('name', 'us_state', 'date_visited', 'lat', 'lon')

class country_admin(admin.ModelAdmin):
    list_display = ('name', 'flag')

admin.site.register(Photo, photo_admin)
admin.site.register(Capital, capital_admin)
admin.site.register(Country, country_admin)
