from django.contrib import admin

from Insta.models import Post, InstaUser

# Register your models here if you want it appear in the admin.

admin.site.register(Post)
admin.site.register(InstaUser)