from django.urls import path
from . import views  # Assuming your views are defined in `products.views.py`

urlpatterns = [
    path('', views.base, name='base'),
    # ... other product-related URL patterns
]
