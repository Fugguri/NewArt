from django.contrib import admin
from .models import Paint, Year, Collection, Material, Orientation, BookmarksModel


class PaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'pub_date',
                    'collection', 'materials', 'year', 'orientation')
    search_fields = ('title', 'description', )
    list_editable = ('collection', 'year', 'materials', 'orientation')
    search_fields = ('collection', 'year')
    list_display_links = ('id', 'title',)


admin.site.register(Paint, PaintAdmin)
admin.site.register(Year)
admin.site.register(Collection)
admin.site.register(Material)
admin.site.register(Orientation)
admin.site.register(BookmarksModel)
