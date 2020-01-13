from rest_framework import serializers

from products.models import Manufacturer, Store, Product, Ingredient, BeneficialIngredient, Effect, Organ, Quantity, Form, SearchLog


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class OrganSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organ
        fields = ('__all__')


class EffectSerializer(serializers.ModelSerializer):
    organ = serializers.SerializerMethodField()

    class Meta:
        model = Effect
        fields = ('__all__')

    def get_organ(self, obj):
        organ = OrganSerializer(obj.organ.all(), many=True).data
        return organ


class BeneficialIngredientSerializer(serializers.ModelSerializer):
    effect = serializers.SerializerMethodField()

    class Meta:
        model = BeneficialIngredient
        fields = ('__all__')

    def get_effect(self, obj):
        effect = EffectSerializer(obj.effect.all(), many=True).data
        return effect


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ('__all__')


class IngredientSerializer(serializers.ModelSerializer):
    beneficial_ingredient = serializers.SerializerMethodField()
    ingredient_quantity = StringSerializer(many=False)

    class Meta:
        model = Ingredient
        fields = ('__all__')

    def get_beneficial_ingredient(self, obj):
        beneficial_ingredient = BeneficialIngredientSerializer(obj.beneficial_ingredient.all(), many=True).data
        return beneficial_ingredient


class ProductSerializer(serializers.ModelSerializer):
    manufacture = StringSerializer(many=False)
    form = StringSerializer(many=False)
    ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('__all__')
    
    def get_ingredients(self, obj):
        ingredients = IngredientSerializer(obj.ingredients.all(), many=True).data
        return ingredients


class StoreSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ('__all__')

    def get_products(self, obj):
        products = ProductSerializer(obj.products.all(), many=True).data
        return products
