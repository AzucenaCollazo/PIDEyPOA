from django.db import models

# Create your models here.
class login(models.Model):
    usuario = models.EmailField(max_length=254, verbose_name="Nombre")
    password = models.CharField(max_length=10)
    

class programas(models.Model):
    nombre = models.CharField(max_length=254, verbose_name="Nombre")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class estrategias(models.Model):
    nombre = models.CharField(max_length=254, verbose_name="Nombre")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class areas(models.Model):
    nombre = models.CharField(max_length=254, verbose_name="Nombre")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class indicadores(models.Model):
    nombre = models.CharField(max_length=254, verbose_name='Nombre')
    estrategia = models.ForeignKey( estrategias, on_delete=models.CASCADE)
    programa = models.ForeignKey( programas, on_delete=models.CASCADE)
    area = models.ForeignKey( areas, on_delete=models.CASCADE)
    Resultado2020 = models.CharField( max_length=254, verbose_name='Resultado2020')
    Resultado2021 = models.CharField( max_length=254, verbose_name='Resultado2021')
    Resultado2022 = models.CharField( max_length=254, verbose_name='Resultado2022')
    SED2023 = models.CharField( max_length=254, verbose_name='SED2023')
    PIDE2023 = models.CharField( max_length=254, verbose_name='PIDE2023')
    POADGUTyP2023 = models.CharField( max_length=254, verbose_name='POADGUTyP2023')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
