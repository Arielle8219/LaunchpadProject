from django.contrib import admin
from .models import TreeLoss

class TreeLossAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(TreeLoss, TreeLossAdmin)