import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangomart.settings")
django.setup()

from store.models import Product

def update_existing_records():
    # Retrieve all existing Product objects
    products = Product.objects.all()

    # Loop through each product and update the image fields if they are empty
    for product in products:
        if not product.image1:
            product.image1 = "default/default_image1.jpg"  # Set default image path
        if not product.image2:
            product.image2 = "default/default_image2.jpg"  # Set default image path
        if not product.image3:
            product.image3 = "default/default_image3.jpg"  # Set default image path

        # Save the updated product
        product.save()

if __name__ == "__main__":
    update_existing_records()
