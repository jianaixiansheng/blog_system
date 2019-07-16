from django.contrib import admin
from .models import *
# Register your models here.
class Photoalbum(admin.ModelAdmin):
    list_display = ["image_type","user_image"]

admin.site.register(PhotoAlbum,Photoalbum)

class Photograph(admin.ModelAdmin):
    list_display = ["user_image_url"]

admin.site.register(PhotoGraph,Photograph)