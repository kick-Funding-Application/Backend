from django.contrib import admin
from .models import Project, Thumbnail


# Register your models here.
class ThumbnailInline(admin.TabularInline):
    model = Thumbnail
    extra = 0


class ThumbnailAdmin(admin.ModelAdmin):
    inlines = [
        ThumbnailInline,
    ]


admin.site.register(Project, ThumbnailAdmin)
admin.site.register(Thumbnail)
