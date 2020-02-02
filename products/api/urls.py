# from django.conf.urls import url

# from .views import ProductListView, ProductDetailView


# urlpatterns = [
#    url(r'^$', ProductListView.as_view()),
#    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view())
# ]


from products.api.views import ProductViewSet, BeneficialIngredientViewSet, EffectViewSet, IngredientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'bing', BeneficialIngredientViewSet, basename='beneficialIngredient')
router.register(r'bi', IngredientViewSet, basename='Ingredient')
router.register(r'effects', EffectViewSet, basename='effects')
urlpatterns = router.urls
