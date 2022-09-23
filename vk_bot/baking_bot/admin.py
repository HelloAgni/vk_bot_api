from django.contrib import admin

from .models import SimpleText, Baking, BakingType, Image


class SimpleTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто'


class BakingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    search_fields = ('type',)
    list_filter = ('type',)
    empty_value_display = '-пусто'


class BakingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'type')
    search_fields = ('title', 'type')
    list_filter = ('title', 'type')
    empty_value_display = '-пусто'


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_file', 'image_b64')


admin.site.register(Baking, BakingAdmin)
admin.site.register(BakingType, BakingTypeAdmin)
admin.site.register(SimpleText, SimpleTextAdmin)
admin.site.register(Image, ImageAdmin)
