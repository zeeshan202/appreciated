#from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework import viewsets

from products.models import Product, BeneficialIngredient, Effect, Ingredient
from .serializers import ProductSerializer, BeneficialIngredientSerializer, EffectSerializer, IngredientSerializer


# class ProductListView(ListAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer


#class ProductDetailView(RetrieveAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    serializer_class = ProductSerializer
    def get_queryset(self):
        searchValue = self.request.query_params.get('searchValue', "")
        if searchValue:
            searchValue = [int(x.strip()) for x in searchValue.split(',') if x]
            queryset = Product.objects.all()
            queryset = queryset.filter(ingredients__id__in=searchValue)#.exclude(ingredients__id__in=[3])
        searchValue = self.request.query_params.get('productsValue', "")
        if searchValue:
            searchValue = [int(x.strip()) for x in searchValue.split(',') if x]
            queryset = Product.objects.all()
            queryset = queryset.filter(id__in=searchValue)#.exclude(ingredients__id__in=[3])
        #beneficialingredient = BeneficialIngredient.objects.filter(effect__id__in=[benefitID])
        return queryset


class IngredientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    
    serializer_class = IngredientSerializer
    def get_queryset(self):
        benefitID = self.request.query_params.get('benefitID', None)
        #beneficialingredient = BeneficialIngredient.objects.filter(effect__id__in=[benefitID])
        queryset = Ingredient.objects.all()
        queryset = queryset.filter(beneficial_ingredient__effect__id__in=[benefitID])
        return queryset


class BeneficialIngredientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    serializer_class = BeneficialIngredientSerializer
    
    def get_queryset(self):
        queryset = BeneficialIngredient.objects.all()
        benefitID = self.request.query_params.get('benefitID', None)
        #queryset = queryset.filter(beneficialingredient__name__contains=searchValue)#ascorbic acid
        queryset = queryset.filter(effect__id__in=[benefitID])
        return queryset


class EffectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    serializer_class = EffectSerializer
    def get_queryset(self):
        queryset = Effect.objects.all()
        searchValue = self.request.query_params.get('searchValue', None)
        #queryset = queryset.filter(beneficialingredient__name__contains=searchValue)#ascorbic acid
        queryset = queryset.filter(name__contains=searchValue)
        return queryset

