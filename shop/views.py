from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Product, Category, PageContent, ContactMessage
from .forms import ContactForm
import urllib.parse
import logging

logger = logging.getLogger(__name__)


def contact_page(request):
    """Dedicated contact page with form submission, email notification, and WhatsApp share."""
    # Load the PageContent for editable hero/text (optional, won't crash if missing)
    try:
        page = PageContent.objects.get(slug='contact')
    except PageContent.DoesNotExist:
        page = None

    success = False
    whatsapp_url = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()

            # --- Email Notification ---
            try:
                from django.core.mail import send_mail
                from django.conf import settings
                subject = f"[GOURME] New Contact Inquiry from {msg.name}"
                body = (
                    f"New contact form submission:\n\n"
                    f"Name: {msg.name}\n"
                    f"Phone: {msg.phone}\n"
                    f"Email: {msg.email}\n"
                    f"Query: {msg.query}\n\n"
                    f"Submitted at: {msg.created_at}\n"
                    f"---\n"
                    f"View in admin: {request.build_absolute_uri('/admin/shop/contactmessage/')}"
                )
                owner_email = getattr(settings, 'CONTACT_NOTIFY_EMAIL', None)
                if owner_email:
                    send_mail(
                        subject,
                        body,
                        settings.DEFAULT_FROM_EMAIL,
                        [owner_email],
                        fail_silently=True,
                    )
                    logger.info(f"Contact notification email sent to {owner_email}")
                else:
                    logger.info("CONTACT_NOTIFY_EMAIL not set — skipping email notification")
            except Exception as e:
                logger.warning(f"Email notification failed: {e}")

            # --- WhatsApp Share Link ---
            wa_message = (
                f"🍄 *New GOURME Inquiry*\n\n"
                f"*Name:* {msg.name}\n"
                f"*Phone:* {msg.phone}\n"
                f"*Email:* {msg.email}\n"
                f"*Query:* {msg.query}"
            )
            whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(wa_message)}"

            success = True
            form = ContactForm()  # Reset form after success
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'page': page,
        'form': form,
        'success': success,
        'whatsapp_url': whatsapp_url,
    })

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

def shop(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

from django.shortcuts import get_object_or_404

def page_detail(request, slug):
    page = get_object_or_404(PageContent, slug=slug)
    products = page.featured_products.all()
    articles = page.articles.filter(is_published=True).prefetch_related('blocks')
    return render(request, 'page_detail.html', {
        'page': page,
        'products': products,
        'articles': articles,
    })

def api_products(request):
    category_slug = request.GET.get('category')
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else:
        products = Product.objects.all()
    
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'category': p.category.title if p.category else '',
            'price': str(p.price),
            'primary_image': request.build_absolute_uri(p.primary_image.url) if p.primary_image else '',
            'hover_image': request.build_absolute_uri(p.hover_image.url) if p.hover_image else '',
        })
    return JsonResponse(data, safe=False)

def api_categories(request):
    categories = Category.objects.all()
    data = []
    for c in categories:
        data.append({
            'id': c.id,
            'slug': c.slug,
            'title': c.title,
            'hex_color': c.hex_color,
            'image': request.build_absolute_uri(c.image.url) if c.image else '',
        })
    return JsonResponse(data, safe=False)

def api_category_detail(request, slug):
    try:
        c = Category.objects.get(slug=slug)
        data = {
            'id': c.id,
            'slug': c.slug,
            'title': c.title,
            'page_description': c.page_description,
            'hero_image': request.build_absolute_uri(c.hero_image.url) if c.hero_image else '',
            'hex_color': c.hex_color,
        }
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def api_page_detail(request, slug):
    try:
        p = PageContent.objects.get(slug=slug)
        data = {
            'id': p.id,
            'slug': p.slug,
            'title': p.title,
            'sub_headline': p.sub_headline,
            'body_text': p.body_text,
            'hero_image': request.build_absolute_uri(p.hero_image.url) if p.hero_image else '',
        }
        return JsonResponse(data)
    except PageContent.DoesNotExist:
        return JsonResponse({'error': 'Page not found'}, status=404)
