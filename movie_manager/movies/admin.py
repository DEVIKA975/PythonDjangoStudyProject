from django.contrib import admin
from .models import CensorInfo, DirectorInfo, MovieInfo, actorInfo
# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(DirectorInfo)
admin.site.register(CensorInfo)
admin.site.register(actorInfo)
