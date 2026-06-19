from django.contrib import admin
from .models import Opinion


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calificacion', 'activa', 'fecha')
    list_filter = ('calificacion', 'activa')
    search_fields = ('nombre', 'correo', 'texto')
    list_editable = ('activa',)
    readonly_fields = ('fecha',)
    ordering = ('-fecha',)
