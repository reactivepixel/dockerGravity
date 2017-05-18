from django.contrib import admin

# Register your models here.
from api.models import Track,Set,Setlist,TrackPosition,SetlistPosition

admin.site.register(Track)
admin.site.register(Set)
admin.site.register(Setlist)
admin.site.register(TrackPosition)
admin.site.register(SetlistPosition)
