from django.contrib import admin
from .models import Profile
# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_view=[
        'title',
        'description',
        'creation',
        'thumbnail',
    ]
admin.site.register(Profile,AdminProfile)