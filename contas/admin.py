from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)
