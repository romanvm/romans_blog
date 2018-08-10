from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration

SingletonModelAdmin.save_on_top = True
admin.site.register(SiteConfiguration, SingletonModelAdmin)
