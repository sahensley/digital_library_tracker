from django.contrib import admin

from .models import Application, Bundle, Developer, HumbleItem, Person, Publisher

admin.site.register(Application)
admin.site.register(Bundle)
admin.site.register(Developer)
admin.site.register(HumbleItem)
admin.site.register(Person)
admin.site.register(Publisher)
