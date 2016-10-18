from django.contrib import admin
from .models import Meeting, Member, Point


admin.site.register(Meeting)
admin.site.register(Member)
admin.site.register(Point)