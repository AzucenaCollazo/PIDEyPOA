from django.contrib import admin
from .models import indicadores
from .models import estrategias
from .models import areas
from .models import programas
from .models import login
# Register your models here.
admin.site.register(indicadores)
admin.site.register(estrategias)
admin.site.register(areas)
admin.site.register(programas)
admin.site.register(login)