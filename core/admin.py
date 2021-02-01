from django.contrib import admin

from .models import Application, Developer, Person, Platform, Publisher

admin.site.register(Application)
admin.site.register(Developer)
admin.site.register(Person)
admin.site.register(Platform)
admin.site.register(Publisher)
