from django.contrib import admin
from .models import (
    Product, Category, PageContent, ContactMessage, Article, ContentBlock,
    ShopProduct, ShopCategory, ShopPage, 
    DiscoverArticle, DiscoverPage, 
    ValuePage, 
    UtilityContact, UtilityPage
)
from django_summernote.admin import SummernoteModelAdmin

# --- CUSTOM ADMIN SITE FOR GROUPING ---

class GourmeAdminSite(admin.AdminSite):
    site_header = "GOURME Marketplace Administration"
    site_title = "GOURME Admin"
    index_title = "Welcome to GOURME Control Center"

    def get_app_list(self, request):
        """
        Customizes the admin index to group models into Shop, Discover, Value, and Utility.
        """
        app_dict = self._build_app_dict(request)
        
        # Categorization mapping
        groups = {
            'SHOP': ['ShopProduct', 'ShopCategory', 'ShopPage'],
            'DISCOVER': ['DiscoverArticle', 'DiscoverPage'],
            'VALUE': ['ValuePage'],
            'UTILITY': ['UtilityContact', 'UtilityPage'],
        }
        
        # Reconstruct the app list
        new_app_list = []
        
        # Collect all models from the 'shop' app
        all_models = {}
        if 'shop' in app_dict:
            for m in app_dict['shop']['models']:
                all_models[m['object_name']] = m
        
        # Create categories as "apps" in the sidebar
        for group_name, model_names in groups.items():
            group_models = []
            for name in model_names:
                if name in all_models:
                    group_models.append(all_models[name])
            
            if group_models:
                new_app_list.append({
                    'name': group_name,
                    'app_label': group_name.lower(),
                    'models': group_models,
                    'has_module_perms': True,
                })
        
        # Keep other apps (like Summernote, Auth) at the bottom
        for app_label, app in app_dict.items():
            if app_label != 'shop':
                new_app_list.append(app)
                
        return new_app_list

# Create instance
gourme_admin = GourmeAdminSite(name='gourme_admin')


# --- SHARED ADMIN MIXINS ---

class PageProxyAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('featured_products',)
    summernote_fields = ('body_text',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug__in=self.slug_list)

    def product_count(self, obj):
        return obj.featured_products.count()
    product_count.short_description = 'Products'

    def article_count(self, obj):
        return obj.articles.count()
    article_count.short_description = 'Articles'


# --- REGISTRATIONS ---

@admin.register(ShopProduct, site=gourme_admin)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

@admin.register(ShopCategory, site=gourme_admin)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'hex_color')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ShopPage, site=gourme_admin)
class ShopPageAdmin(PageProxyAdmin):
    slug_list = ['products', 'extracts', 'best-sellers', 'new-products']
    list_display = ('title', 'slug', 'product_count')


class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 1
    ordering = ['order']
    fieldsets = (
        (None, {'fields': ('block_type', 'order')}),
        ('Text Content', {'classes': ('collapse',), 'fields': ('text_content',)}),
        ('Media', {'classes': ('collapse',), 'fields': ('image', 'image_caption', 'video_url')}),
    )

@admin.register(DiscoverArticle, site=gourme_admin)
class DiscoverArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'page', 'is_published', 'published_date', 'order')
    list_filter = ('page', 'is_published', 'published_date')
    search_fields = ('title', 'summary')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('order', 'is_published')
    summernote_fields = ('summary', 'content')
    inlines = [ContentBlockInline]

@admin.register(DiscoverPage, site=gourme_admin)
class DiscoverPageAdmin(PageProxyAdmin):
    slug_list = ['benefits', 'recipes', 'foraging-guides', 'story']
    list_display = ('title', 'slug', 'article_count')


@admin.register(ValuePage, site=gourme_admin)
class ValuePageAdmin(PageProxyAdmin):
    slug_list = ['offers', 'promos', 'combos', 'subscription-plans']
    list_display = ('title', 'slug', 'product_count')


@admin.register(UtilityContact, site=gourme_admin)
class UtilityContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'phone', 'query')
    readonly_fields = ('name', 'phone', 'email', 'query', 'created_at', 'whatsapp_link')
    
    def whatsapp_link(self, obj):
        from django.utils.html import format_html
        import urllib.parse
        message = f"Hi {obj.name}, thank you for reaching out to GOURME!"
        encoded = urllib.parse.quote(message)
        wa_url = f"https://wa.me/{obj.phone}?text={encoded}"
        return format_html('<a href="{}" target="_blank" style="padding:5px 10px; background:#25D366; color:white; border-radius:3px;">Reply on WhatsApp</a>', wa_url)

@admin.register(UtilityPage, site=gourme_admin)
class UtilityPageAdmin(PageProxyAdmin):
    slug_list = ['contact', 'account', 'shipping-returns']

# Register Summernote and Auth to the custom site as well
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
gourme_admin.register(User, UserAdmin)
gourme_admin.register(Group, GroupAdmin)

try:
    from django_summernote.models import Attachment
    from django_summernote.admin import AttachmentAdmin
    gourme_admin.register(Attachment, AttachmentAdmin)
except:
    pass
