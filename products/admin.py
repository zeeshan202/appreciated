from django.contrib import admin

# Register your models here.

from .models import Manufacturer, Store, Product, Ingredient, BeneficialIngredient, Effect, Organ, Quantity, Form, SearchLog

admin.site.register(Manufacturer)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Ingredient)
admin.site.register(BeneficialIngredient)
admin.site.register(Effect)
admin.site.register(Organ)
admin.site.register(Quantity)
admin.site.register(Form)
admin.site.register(SearchLog)
