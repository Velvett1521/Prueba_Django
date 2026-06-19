from django.db import models


class Opinion(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    texto = models.TextField()
    calificacion = models.PositiveSmallIntegerField(
        choices=[(i, f'{i} estrella{"s" if i > 1 else ""}') for i in range(1, 6)]
    )
    fecha = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)  # para moderar desde el admin

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Opinión'
        verbose_name_plural = 'Opiniones'

    def __str__(self):
        return f'{self.nombre} — {self.calificacion}★'
