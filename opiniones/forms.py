from django import forms
from .models import Opinion


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['nombre', 'correo', 'calificacion', 'texto']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej. Carlos M.',
            }),
            'correo': forms.EmailInput(attrs={
                'placeholder': 'tu@correo.com',
            }),
            'texto': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Cuéntanos tu experiencia...',
            }),
        }
        labels = {
            'nombre': 'Tu nombre',
            'correo': 'Correo electrónico',
            'calificacion': 'Calificación',
            'texto': 'Tu opinión',
        }
