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
            searchValue = [str(x.strip()) for x in searchValue.split(',') if x]
            queryset = Product.objects.all()
            queryset = queryset.filter(ingredients__name__in=searchValue)#.exclude(ingredients__id__in=[3])
        searchValue = self.request.query_params.get('ManufactureValue', "")
        if searchValue:
            ProductsArray = self.request.query_params.get('ProductsArray', "")
            ProductsArray = [str(x.strip()) for x in ProductsArray.split(',') if x]
            searchValue = [str(x.strip()) for x in searchValue.split(',') if x]
            queryset = Product.objects.all()
            queryset = queryset.filter(ingredients__name__in=searchValue)#.exclude(ingredients__id__in=[3])
            queryset = queryset.filter(manufacture__name__in=ProductsArray)#.exclude(ingredients__id__in=[3]) 'AB Matrix s.r.o.','Alveola Kft.' ['Béres Pharmaceuticals Ltd..']
        searchValue = self.request.query_params.get('BenefitValue', None)
        if searchValue:
            searchValue = [str(x.strip()) for x in searchValue.split(',') if x]
            queryset = Product.objects.all()
            queryset = queryset.filter(ingredients__beneficial_ingredient__effect__name__in=searchValue)
            #queryset = queryset.filter(manufacture__name__in=searchValue)#.exclude(ingredients__id__in=[3])
            #queryset = queryset.filter(manufacture__name__in=['AB Matrix s.r.o.','Alveola Kft.'])#.exclude(ingredients__id__in=[3])
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
        searchValue = self.request.query_params.get('searchValue', "")
        queryset = Ingredient.objects.all()
        #queryset = queryset.filter(name__contains=searchValue)#.exclude(ingredients__id__in=[3])
        benefitID = self.request.query_params.get('benefitID', "")
        if benefitID:
            searchValue = [int(x.strip()) for x in benefitID.split(',') if x]
            #beneficialingredient = BeneficialIngredient.objects.filter(effect__id__in=[benefitID])
            queryset = Ingredient.objects.all()
            queryset = queryset.filter(beneficial_ingredient__effect__id__in=searchValue)
        searchValue = self.request.query_params.get('searchValueIds', "")
        if searchValue:
            searchValue = [str(x.strip()) for x in searchValue.split(',') if x]
            queryset = Ingredient.objects.all()
            queryset = queryset.filter(name__in=searchValue)#.exclude(ingredients__id__in=[3])
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
        searchValue = self.request.query_params.get('searchValueIds', "")
        if searchValue:
            searchValue = [int(x.strip()) for x in searchValue.split(',') if x]
            queryset = BeneficialIngredient.objects.all()
            queryset = queryset.filter(ingredient__id__in=searchValue)#.exclude(ingredients__id__in=[3])
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

