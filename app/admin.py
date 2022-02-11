from django.contrib import admin
from .models import UserModel
# Register your models here.

admin.site.site_header = "Hotel Recommendation System"
admin.site.site_title = "KITE Admin Portal"
admin.site.index_title = "Welcome to KITE"


@admin.register(UserModel)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'gender', 'date_created']
