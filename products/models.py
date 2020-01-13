from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
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
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organ = models.ManyToManyField(Organ)

    def __str__(self):
        return self.name


class BeneficialIngredient(models.Model):
    name = models.CharField(max_length=120)
    preparation = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    effect = models.ManyToManyField(Effect)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.CharField(max_length=120, default='')
    unit = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    form_quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    beneficial_ingredient = models.ManyToManyField(BeneficialIngredient)
    ingredient_quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    registration_number = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product', blank=True)
    manufacture = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1)
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

