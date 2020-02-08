from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Organ(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Effect(models.Model):

    SELECT = 'SE'
    EVIDENCE = 'ED'
    ANECDOTAL = 'AD'
    EFSA = 'EA'
    
    EffectOfType = [
        (SELECT, ''),
        (EVIDENCE, 'Evidence'),
        (ANECDOTAL, 'Anecdotal'),
        (EFSA, 'EFSA'),
    ]
    
    name = models.CharField(max_length=120)
    detail = models.TextField()
    dose = models.CharField(max_length=120)
    oftype = models.CharField(
        max_length=2,
        choices=EffectOfType,
        default=SELECT,
    )
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organ = models.ManyToManyField(Organ, blank=True)

    def __str__(self):
        return self.name


class BeneficialIngredient(models.Model):
    name = models.CharField(max_length=120)
    preparation = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    effect = models.ManyToManyField(Effect, blank=True)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.CharField(max_length=120, default='')
    #   models.DecimalField(..., max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    form_quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    SELECT = 'SE'
    ACTIVE = 'AC'
    INACTIVE = 'IA'
    
    IngredientOfType = [
        (SELECT, ''),
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    
    name = models.CharField(max_length=120)
    oftype = models.CharField(
        max_length=2,
        choices=IngredientOfType,
        default=SELECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    beneficial_ingredient = models.ManyToManyField(BeneficialIngredient, blank=True)
    ingredient_quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField()
    caution = models.CharField(max_length=120, blank=True)
    registration_number = models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product', blank=True)
    manufacture = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1, related_name='manuf')
    ingredients = models.ManyToManyField(Ingredient)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class SearchLog(models.Model):
    search_query = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

