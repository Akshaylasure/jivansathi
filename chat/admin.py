from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)


from django.contrib import admin

# Register your models here.
from chat.models import Roles
from chat.models import Profile

# Register your models here.
admin.site.register(Roles)
admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'gender', 'mobile', 'city')
    search_fields = ('name', 'username', 'gender')