from django.db import models

class Chab(models.Model):
	chab = models.IntegerField(blank=False, null=False, verbose_name = "Año")
	imagenChab = models.ImageField('Imagen de Cargador', upload_to='qamar_images', default=None)

	class Meta:
		verbose_name = "Año"
		verbose_name_plural = "Años"

	def __str__(self):
		return str(self.chab)

class Cuatrimestre(models.Model):
    #idChab = models.ForeignKey(Chab, on_delete=models.CASCADE, verbose_name = "Año")
    nombreCuatrimestre = models.CharField(max_length=25, verbose_name = "Cuatrimestre")

    class Meta:
    	verbose_name = "Cuatrimestre"
    	verbose_name_plural = "Cuatrimestres"

    def __str__(self):
    	return self.nombreCuatrimestre

class Tiempo(models.Model):
	nombreTiempo = models.CharField('Tiempo', max_length = 25)

	class Meta:
		verbose_name = "Tiempo del año"
		verbose_name_plural = "Tiempos del año"

	def __str__(self):
		return self.nombreTiempo

class Epoca(models.Model):
	nombreEpoca = models.CharField('Época', max_length = 25)

	class Meta:
		verbose_name = "Época del año"
		verbose_name_plural = "Épocas del año"

	def __str__(self):
		return self.nombreEpoca

class Mes(models.Model):
	nombreMes = models.CharField('Mes', max_length=15)
	idCuatrimestre = models.ForeignKey(Cuatrimestre, on_delete=models.CASCADE, verbose_name = "Cuatrimestre")
	idTiempo = models.ForeignKey( Tiempo, on_delete=models.CASCADE, verbose_name = "Tiempo del año" )
	idEpoca = models.ForeignKey( Epoca, on_delete=models.CASCADE, verbose_name = "Época del año")

	class Meta:
		verbose_name = "Mes"
		verbose_name_plural = "Meses"

	def __str__(self):
		return self.nombreMes

	def getCuatrimestre(self):
		return str(self.idCuatrimestre)

	def getTiempo(self):
		return str(self.idTiempo)

	def getEpoca(self):
		return str(self.idEpoca)

class Fase(models.Model):
	nombreFase = models.CharField('Fase Lunar', max_length = 25)
	imagenFase = models.ImageField('Imagen de Luna', upload_to='qamar_images', default=None)

	class Meta:
		verbose_name = "Fase lunar"
		verbose_name_plural = "Fases lunares"

	def __str__(self):
		return self.nombreFase

class LunaMes( models.Model ):
	fecha = models.IntegerField('Fecha Lunar', blank=False, null=False)
	idFase = models.ForeignKey(Fase, on_delete=models.CASCADE, verbose_name = "Fase Lunar")
	idMes = models.ForeignKey(Mes, on_delete=models.CASCADE, verbose_name = "Mes")
	idChab = models.ForeignKey(Chab, on_delete=models.CASCADE, verbose_name = "Año")
	
	class Meta:
		verbose_name = "Fecha lunar"
		verbose_name_plural = "Fechas lunares"

	def __str__(self):
		return str(self.fecha)+"/"+self.idMes.nombreMes+"/"+str(self.idChab)

	def getFase(self):
		return str(self.idFase)

	def getMes(self):
		return str(self.idMes)

class TipoActividad(models.Model):
	nombreTipoActividad = models.CharField('Tipo de Actividad', max_length = 200)

	class Meta:
		verbose_name = "Tipo de actividad"
		verbose_name_plural = "Tipos de actividades"

	def __str__(self):
		return self.nombreTipoActividad

class Actividad(models.Model):
	nombreActividad = models.CharField(max_length = 200, verbose_name = "Nombre de Actividad")
	descripcion = models.TextField(default=None, verbose_name = "Descripción de Actividad")
	idTipoActividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE, verbose_name = "Tipo de Actividad")

	class Meta:
		verbose_name = "Actividad"
		verbose_name_plural = "Actividades"

	def __str__(self):
		return self.nombreActividad

	def getTipoActividad(self):
		return str(self.idTipoActividad)

class LunaActividad(models.Model):
	idFecha = models.ForeignKey(LunaMes, on_delete=models.CASCADE, verbose_name = "Fecha Lunar")
	idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, verbose_name = "Actividad")
	
	class Meta:
		verbose_name = "Activad por fecha"
		verbose_name_plural = "Actividades por fecha"

	def fechaActividad(self):
		return str(self.idFecha)

class LogosPieDePagina(models.Model):
	nombreLogo = models.CharField('Nombre de Logo', max_length = 25)
	imagenLogo = models.ImageField('Imagen', upload_to='qamar_images', default=None)

	class Meta:
		verbose_name = "Logo pie de página"
		verbose_name_plural = "Logos pie de página"

	def __str__(self):
		return self.nombreLogo