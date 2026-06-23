from django.contrib import admin
from django.utils.html import format_html
from .models import Opinion


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calificacion', 'tiene_imagen', 'activa', 'fecha')
    list_filter = ('calificacion', 'activa')
    search_fields = ('nombre', 'correo', 'texto')
    list_editable = ('activa',)
    readonly_fields = ('fecha', 'preview_imagen')
    ordering = ('-fecha',)

    def tiene_imagen(self, obj):
        return '🖼️' if obj.imagen else '—'
    tiene_imagen.short_description = 'Imagen'

    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height:200px; border-radius:8px;" />',
                obj.imagen.url
            )
        return 'Sin imagen'
    preview_imagen.short_description = 'Vista previa'

    fields = (
        'nombre', 'correo', 'calificacion',
        'texto', 'imagen', 'preview_imagen',
        'activa', 'fecha'
    )
