import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from shop.models import PageContent, Product

# Verify the featured_products field
page = PageContent.objects.get(slug='best-sellers')
print(f"Page: {page.title}")
print(f"Featured products field exists: {hasattr(page, 'featured_products')}")
print(f"Current featured products: {page.featured_products.count()}")
print(f"Available products total: {Product.objects.count()}")
print()

# List all pages
print("=== ALL PAGES ===")
for p in PageContent.objects.all().order_by('slug'):
    print(f"  {p.slug} -> {p.title} (products: {p.featured_products.count()})")
