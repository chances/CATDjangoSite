from django.contrib import admin
from newzuul.models import consumer, items

# Register your models here.

class itemsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name:', {'fields': ['name']}),
        ('Price of item:', {'fields': ['price']}),
    ]

    list_display = ('name', 'price')
    #list_filter = ['name']
    search_fields = ['name']

class consumerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name:', {'fields': ['name']}),
        ('Ammount in bank:', {'fields': ['bank']}),
    ]

    list_display = ('name', 'bank')
    #list_filter = ['name']
    search_fields = ['name']

admin.site.register(consumer, consumerAdmin)
admin.site.register(items, itemsAdmin)