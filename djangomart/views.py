from django.shortcuts import render
from store.models import Product

def home(request):
    # Define category names and corresponding product counts in a dictionary
    category_data = {
        "Bags": 4,
        "Shoes": 4,
        "Coats": 4,
        "Watches": 4,
        "T-Shirts": 4,
        "Shirts": 4,
        "Jeans": 4,
        # Add more categories here as needed
    }

    # Create an empty dictionary to store products for each category
    category_products = {}

    for category_name, product_count in category_data.items():
        # Filter and retrieve the top N most sold products of the category
        category_products[category_name] = Product.objects.filter(category__category_name=category_name).order_by('-sold')[:product_count]

    context = {
        'category_products': category_products,
    }
    return render(request, 'home.html', context)
