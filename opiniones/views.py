from django.shortcuts import render, redirect
from .models import Opinion
from .forms import OpinionForm


def inicio(request):
    total = Opinion.objects.filter(activa=True).count()
    return render(request, 'inicio.html', {'total': total})


def dejar_opinion(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('opinion_enviada')
    else:
        form = OpinionForm()
    return render(request, 'dejar_opinion.html', {'form': form})


def opinion_enviada(request):
    return render(request, 'opinion_enviada.html')


def ver_opiniones(request):
    opiniones = Opinion.objects.filter(activa=True)
    return render(request, 'ver_opiniones.html', {'opiniones': opiniones})
