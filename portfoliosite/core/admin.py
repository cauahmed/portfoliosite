from django.contrib import admin

from .views import *

from.models import Contact

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(CompletedProject)
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Certification)