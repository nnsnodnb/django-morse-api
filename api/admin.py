from django.contrib import admin
from .models import ReceiveSentence

class ReceiveSentenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sentence', 'receive_date')
    list_display_links = ('id', 'sentence', 'receive_date')

admin.site.register(ReceiveSentence, ReceiveSentenceAdmin)
