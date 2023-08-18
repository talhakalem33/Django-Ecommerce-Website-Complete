from django.contrib import admin
from .models import Product, Category, Campaigns, Descriptions

class ProductAdmin(admin.ModelAdmin):
    list_display = ("Name", "isActive")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("CategoryName", "isActive")

class CampaignAdmin(admin.ModelAdmin):
    list_display = ("Name", "isActive")

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Campaigns, CampaignAdmin)
admin.site.register(Descriptions)