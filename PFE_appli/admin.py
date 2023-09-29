from django.contrib import admin
from .models import Village, Foret, Foret_sacree
# Register your models here.

class AdminVillage(admin.ModelAdmin):
    list_display = ('village', 'nombre_de_forêts')


class AdminForet_Sacree(admin.ModelAdmin):
    list_display = ('nom_du_responsable', 'superficie_en_hectare')
    
class AdminForet(admin.ModelAdmin):
    list_display = ('nom_du_propriétaire','superficie_en_hectare','nature_de_la_forêt')
admin.site.register(Village, AdminVillage)
admin.site.register(Foret, AdminForet)
admin.site.register(Foret_sacree, AdminForet_Sacree)