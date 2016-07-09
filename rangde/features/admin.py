from django.contrib import admin

from features.models import seek_info, investor_info

admin.site.register(seek_info)
admin.site.register(investor_info)
