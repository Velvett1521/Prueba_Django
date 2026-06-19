from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio.html')


def dejar_opinion(request):
    return render(request, 'dejar_opinion.html')


def ver_opiniones(request):
    # Opiniones estáticas de ejemplo (después vendrá la BD)
    opiniones_ejemplo = [
        {
            'nombre': 'Carlos M.',
            'texto': 'Excelente servicio, muy recomendado. La atención fue de primera y el proceso fue super sencillo.',
            'calificacion': 5,
            'fecha': '12 Jun 2025',
        },
        {
            'nombre': 'Sofía R.',
            'texto': 'Buena experiencia en general. El sitio es fácil de usar y el equipo responde rápido.',
            'calificacion': 4,
            'fecha': '8 Jun 2025',
        },
        {
            'nombre': 'Miguel A.',
            'texto': 'Todo perfecto desde el primer momento. Definitivamente volvería a usarlo sin dudarlo.',
            'calificacion': 5,
            'fecha': '1 Jun 2025',
        },
        {
            'nombre': 'Laura T.',
            'texto': 'Muy buen servicio aunque tardó un poco más de lo esperado. Al final todo salió bien.',
            'calificacion': 4,
            'fecha': '25 May 2025',
        },
    ]
    return render(request, 'ver_opiniones.html', {'opiniones': opiniones_ejemplo})
