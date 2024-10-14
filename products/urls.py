from django.urls import path
from .views import ProductCategoryRetrieveUpdateDestroyView, ListCreateProductCategoryView, ListProductCategoryView,ProductRetrieveUpdateDestroyView, ListProductView, ProductListCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product_categories/', ListProductCategoryView.as_view(), name='categories-list-create'),
    path('product_category/<int:pk>/', ProductCategoryRetrieveUpdateDestroyView.as_view(), name='categories-detail'),
    path('create_product_categories/', ListCreateProductCategoryView.as_view(), name='categories-list'),
    path('create_products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('products/', ListProductView.as_view(), name='products-list')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)