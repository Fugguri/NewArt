from django.contrib import admin
from .models import Paint, Year, Collection, Material,Orientation


class PaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description','pub_date','collection','materials','year','orientation')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'description', )
    list_editable =('collection','year','materials','orientation')
    search_fields = ( 'collection','year' )


admin.site.register(Paint,PaintAdmin)
admin.site.register(Year)
admin.site.register(Collection)
admin.site.register(Material)
admin.site.register(Orientation)
