from django.contrib import admin
from django import forms

from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *



class BlogsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogsAdminForm
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    save_as = True
    readonly_fields = ("get_image",)
    search_fields = ("title", )
    list_display = ('title', 'author', 'created_at', 'get_image')
    list_filter = ('category', 'tag', )
    fieldsets = (
        ("Title", {
            "fields": (("title", "slug"),)
        }),
        ("Options", {
            "fields": (("category", "tag"),)
        }),
        ("Content", {
            "fields": (("author", "content"),)
        }),
        ("Image", {
            "fields": (("photo", "get_image"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="549px" height="251px"')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title',)
