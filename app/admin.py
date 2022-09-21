from django.contrib import admin
from .models import destinaton
from .models import guide
from .models import hotel,info,pack

# Register your models here.


admin.site.register(destinaton)
admin.site.register(guide)
admin.site.register(hotel)
admin.site.register(info)
admin.site.register(pack)


