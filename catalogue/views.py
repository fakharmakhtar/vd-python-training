from django.http import HttpResponse, JsonResponse

from .models import Product, Category


def home_view(request):
    return HttpResponse('Hello World!')


def product_list_view(request):
    # Query params
    category = request.GET.get('category')
    # Ternary operator
    queryset = Product.objects.filter(category__name__iexact=category) if category else Product.objects.all()

    max_price = request.GET.get('price')
    if max_price:
        queryset = queryset.filter(price__lte=max_price)

    products = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.display_price,
            'category': product.category.name  # foreign key objects
        }
        for product in queryset
    ]
    return JsonResponse({'products': products})


def product_create_view(request):
    product = Product.objects.create(
        name='Test Product',
        description='test description',
        price=100,
        category=Category.objects.get_or_create(name='Test Category')[0]
    )

    # product = Product(
    #     name='Test Product',
    #     description='test description',
    #     price=100
    # )
    #
    # category, _ = Category.objects.get_or_create(name='Test Category')
    # product.category = category
    # product.save()

    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.display_price,
        'category': product.category.name
    }

    return JsonResponse(product_data)


def product_delete_view(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponse('Product deleted successfully')


def product_update_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return HttpResponse('Product matching the provided id does not exist')

    name = request.GET.get('name')
    if name:
        product.name = name
        product.save()

    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.display_price,
        'category': product.category.name
    }
    return JsonResponse(product_data)
