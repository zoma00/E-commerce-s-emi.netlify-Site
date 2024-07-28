from django.shortcuts import render, redirect
import logging



def base(request):
    context = {
        'api_urls': {
            'product': 'https://semi-netlify-517d375beb38.herokuapp.com/api/Product/',
            'category': 'https://semi-netlify-517d375beb38.herokuapp.com/api/Category/',
            'order': 'https://semi-netlify-517d375beb38.herokuapp.com/api/Order/',
            'order_item': 'https://semi-netlify-517d375beb38.herokuapp.com/api/OrderItem/',
        }
    }
    return render(request, 'products/base.html', context)



logger = logging.getLogger(__name__)

def product_view(request):
    products = Product.objects.all()
    logger.info(f'Products retrieved: {products}')
    return JsonResponse({'products': list(products.values())})

