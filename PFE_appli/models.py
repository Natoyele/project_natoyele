from django.db import models

# Create your models here.
class Village(models.Model):
    village = models.CharField(max_length=200)
    nombre_de_forêts = models.IntegerField()
    
    def __str__(self):
        return self.village
    

class Foret(models.Model):
    village =models.ForeignKey(Village, on_delete= models.CASCADE)
    nom_du_propriétaire = models.CharField(max_length=200)
    superficie_en_hectare = models.DecimalField(max_digits=50, decimal_places=2)
    nature_de_la_forêt = models.CharField(max_length=200)
    
   
    def __str__(self):
        return self.nom_du_propriétaire


class Foret_sacree (models.Model):
    village =models.ForeignKey(Village, on_delete= models.CASCADE)
    nom_du_responsable= models.CharField(max_length=200)
    superficie_en_hectare = models.DecimalField(max_digits=50, decimal_places=2)
    
    def __str__(self):
        return self.nom_du_responsable