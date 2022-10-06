from django.contrib import admin
from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто'


admin.site.register(City, CityAdmin)
