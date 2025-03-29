from django.contrib import admin

from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', #listar
    ordering = '-id', #ordenar
    #list_filter = 'created_date',
    search_fields = 'id','first_name','last_name', #pesquisar
    list_per_page = 10 # a quantidade que vai mostrar
    list_max_show_all = 200 # mostrar no maximo 200
    list_editable = 'first_name', 'last_name', # editar valores sem abrir
    list_display_links = 'id', 'phone',


