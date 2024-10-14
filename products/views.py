from rest_framework import generics
from .models import Product, ProductCategory
from .serializers import ProductCategorySerializer, ProductSerializer
from drf_spectacular.utils import extend_schema

"""
CRUD для категорий
"""


@extend_schema(
    tags=['Категории'],
    description="Получить информацию о всех категориях",
    summary="Получение всех категорий",
    responses={200: ProductCategorySerializer}
)
class ListProductCategoryView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    @extend_schema(
        tags=['Категории'],
        description="Получить информацию о категории по её ID",
        summary="Получение категории",
        responses={200: ProductCategorySerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=['Категории'],
        description="Обновить категорию по её ID",
        summary="Обновление категории",
        request=ProductCategorySerializer,
        responses={200: ProductCategorySerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=['Категории'],
        description="Обновить категорию по её ID",
        summary="Обновление категории",
        request=ProductCategorySerializer,
        responses={200: ProductCategorySerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=['Категории'],
        description="Удалить категорию по её ID",
        summary="Удаление категории",
        responses={204: None}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


@extend_schema(
    tags=['Категории'],
    description="Создать новую категорию продукта",
    summary="Создание категории продукта",
    request=ProductCategorySerializer,
    responses={201: ProductCategorySerializer}
)
class ListCreateProductCategoryView(generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


"""
CRUD для продуктов
"""


@extend_schema(
    tags=['Продукты'],
    description="Получить список всех продуктов с возможностью фильтрации и пагинации.",
    summary="Список продуктов",
    responses={200: ProductSerializer(many=True)},
)
class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        tags=['Продукты'],
        description="Получить информацию о продукте по его ID",
        summary="Получение продукта",
        responses={200: ProductSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=['Продукты'],
        description="Обновить продукт по его ID",
        summary="Обновление продукта",
        request=ProductSerializer,
        responses={200: ProductSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=['Продукты'],
        description="Обновить продукт по его ID",
        summary="Обновление продукта",
        request=ProductSerializer,
        responses={200: ProductSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=['Продукты'],
        description="Удалить продукт по его ID",
        summary="Удаление продукта",
        responses={204: None}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


@extend_schema(
    tags=['Продукты'],
    description="Получить список всех продуктов и создать новый продукт.",
    summary="Список и создание продуктов",
    responses={
        201: ProductSerializer
    }
)
class ProductListCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
