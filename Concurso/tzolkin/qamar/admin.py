from django.contrib import admin
from .models import Chab, Cuatrimestre, Tiempo, Mes, Fase, LunaMes, TipoActividad, Actividad, LunaActividad, Epoca, LogosPieDePagina
# Register your models here.


class ChabAdmin(admin.ModelAdmin):
    list_display = ('chab', 'imagenChab')
    fields = ['chab', 'imagenChab']
    ordering = ('pk',)
admin.site.register(Chab, ChabAdmin)

class CuatrimestreAdmin(admin.ModelAdmin):
	fields = [ 'nombreCuatrimestre' ]
	ordering = ('pk',)
admin.site.register(Cuatrimestre, CuatrimestreAdmin)

class TiempoAdmin(admin.ModelAdmin):
	list_display = ['nombreTiempo']
	fields = [ 'nombreTiempo' ]
	ordering = ('pk',)
admin.site.register(Tiempo, TiempoAdmin)

class EpocaAdmin(admin.ModelAdmin):
	list_display = ['nombreEpoca']
	fields = [ 'nombreEpoca' ]
	ordering = ('pk',)
admin.site.register(Epoca, EpocaAdmin)

class MesAdmin(admin.ModelAdmin):
	list_display = ( 'nombreMes', 'idCuatrimestre', 'idTiempo', 'idEpoca' )
	fields = [ 'nombreMes', 'idCuatrimestre', 'idTiempo', 'idEpoca' ]
	ordering = ('pk',)
admin.site.register(Mes, MesAdmin)

class FaseAdmin(admin.ModelAdmin):
	list_display = ['nombreFase', 'imagenFase']
	fields = ('nombreFase', 'imagenFase')
	ordering = ('pk',)
admin.site.register(Fase, FaseAdmin)

class LunaMesAdmin(admin.ModelAdmin):
	list_display = ( 'fecha', 'idFase', 'idMes', 'idChab')
	fields = ( 'fecha', 'idFase', 'idMes', 'idChab')
	list_filter = ['idChab']
	ordering = ('pk',)
admin.site.register(LunaMes, LunaMesAdmin)

admin.site.register(TipoActividad)

class ActividadAdmin(admin.ModelAdmin):
	list_display = ('nombreActividad','idTipoActividad')
	fields = ('nombreActividad','idTipoActividad', 'descripcion')
	ordering = ('pk',)
admin.site.register(Actividad, ActividadAdmin)

class LunaActividadAdmin(admin.ModelAdmin):
	list_display = ('idFecha', 'idActividad')
	fields = ['idFecha', 'idActividad']
	ordering = ('pk',)
admin.site.register(LunaActividad, LunaActividadAdmin)

class LogosPieDePaginaAdmin(admin.ModelAdmin):
	list_display = ('nombreLogo', 'imagenLogo')
	fields = ('nombreLogo', 'imagenLogo')
	ordering = ('pk',)
admin.site.register(LogosPieDePagina, LogosPieDePaginaAdmin)