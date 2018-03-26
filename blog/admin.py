from django.contrib import admin

from .models import Post, Tag
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated', 'timestamp', 'display_tags')
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Tags', {
            'fields': ('tag',)
        }),
    )
    # fields = ["title", "tag"] - fields that are displayed inside a detail form
    # exclude = ["tag"] - fields not to be displayed in a detail form
    # list_editable = ["title"]
    list_display_links = ["title", "updated"]
    list_filter = ["updated", "timestamp", "tag"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post


admin.site.register(Tag)
