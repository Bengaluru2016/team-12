from django.contrib import admin

from features.models import seek_info_table, investor_info_table

admin.site.register(seek_info_table)
admin.site.register(investor_info_table)
