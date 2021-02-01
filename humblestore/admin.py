from django.contrib import admin

from .models import HumbleBundle, HumbleItem


class HumbleItemAdmin(admin.ModelAdmin):
    list_display = ("__str__", "bundle", "is_gift", "claimed_by")


admin.site.register(HumbleBundle)
admin.site.register(HumbleItem, HumbleItemAdmin)
