from django.contrib import admin

from .models import Jogador, Partida, Indicador, PartidaNota, PartidaIndicador, PartidaGol, \
    PartidaConfirmacao, Clube, Time

admin.site.register(Clube)
admin.site.register(Time)
admin.site.register(Jogador)
admin.site.register(Partida)
admin.site.register(Indicador)
admin.site.register(PartidaNota)
admin.site.register(PartidaIndicador)
admin.site.register(PartidaGol)
admin.site.register(PartidaConfirmacao)
