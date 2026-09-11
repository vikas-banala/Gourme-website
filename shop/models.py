from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200) # e.g. Reishi Immunity
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    primary_image = models.ImageField(upload_to='products/', null=True, blank=True) # Studio shot
    hover_image = models.ImageField(upload_to='products/', null=True, blank=True) # Lifestyle shot

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    hex_color = models.CharField(max_length=7, default='#94A370')
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    hero_image = models.ImageField(upload_to='categories/heroes/', null=True, blank=True)
    page_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class PageContent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    hero_image = models.ImageField(upload_to='pages/heroes/', null=True, blank=True)
    sub_headline = models.CharField(max_length=300, null=True, blank=True)
    body_text = models.TextField(null=True, blank=True)
    featured_products = models.ManyToManyField(
        'Product',
        blank=True,
        related_name='featured_on_pages',
        help_text='Select products to display on this page. Use this for Best Sellers, New Products, Offers, Combos, etc.'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Page Contents"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    email = models.EmailField(max_length=200)
    query = models.TextField(verbose_name='Query / Message')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, help_text='Mark as read after reviewing')

    def __str__(self):
        return f"{self.name} — {self.email} ({self.created_at.strftime('%d %b %Y, %H:%M')})"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']


class Article(models.Model):
    """A blog article / story that belongs to a PageContent (e.g. Mushroom Benefits, Recipes, Our Story)."""
    page = models.ForeignKey(
        PageContent,
        on_delete=models.CASCADE,
        related_name='articles',
        help_text='The page this article belongs to (e.g. Mushroom Benefits, Recipes, Foraging Guides, Our Story).'
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    featured_image = models.ImageField(
        upload_to='articles/featured/',
        null=True, blank=True,
        help_text='Main cover image shown in the article listing card.'
    )
    summary = models.TextField(
        max_length=500,
        null=True, blank=True,
        help_text='Short summary shown on the page listing. 1-2 sentences.'
    )
    content = models.TextField(
        null=True, blank=True,
        help_text='The main blog content. You can add paragraphs, images, and videos here using the rich text editor.'
    )
    published_date = models.DateField(
        null=True, blank=True,
        help_text='Date this article was published. Leave blank for draft.'
    )
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(
        default=0,
        help_text='Lower number = appears first on the page.'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['order', '-published_date']


class ContentBlock(models.Model):
    """A single content block within an Article. Blocks are rendered in order to build up a rich page."""
    BLOCK_TYPES = [
        ('heading', '📝 Heading'),
        ('paragraph', '📄 Paragraph'),
        ('image', '🖼️ Image'),
        ('video', '🎬 Video (YouTube/Vimeo URL)'),
        ('quote', '💬 Quote / Callout'),
        ('divider', '➖ Divider'),
    ]

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='blocks'
    )
    block_type = models.CharField(max_length=20, choices=BLOCK_TYPES, default='paragraph')
    text_content = models.TextField(
        null=True, blank=True,
        help_text='Text for heading, paragraph, or quote blocks.'
    )
    image = models.ImageField(
        upload_to='articles/content/',
        null=True, blank=True,
        help_text='Image for image blocks. Use high-quality photos.'
    )
    image_caption = models.CharField(
        max_length=300,
        null=True, blank=True,
        help_text='Optional caption displayed below the image.'
    )
    video_url = models.URLField(
        null=True, blank=True,
        help_text='YouTube or Vimeo embed URL (e.g. https://www.youtube.com/embed/VIDEO_ID).'
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text='Order within the article. Lower = appears first.'
    )

    def __str__(self):
        label = dict(self.BLOCK_TYPES).get(self.block_type, self.block_type)
        preview = ''
        if self.text_content:
            preview = f' — {self.text_content[:50]}...'
        return f"{label}{preview}"

    class Meta:
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"
        
# --- ADMIN GROUPING PROXIES ---

class ShopProduct(Product):
    class Meta:
        proxy = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ShopCategory(Category):
    class Meta:
        proxy = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ShopPage(PageContent):
    class Meta:
        proxy = True
        verbose_name = 'Shop Page'
        verbose_name_plural = 'Shop Pages'

class DiscoverArticle(Article):
    class Meta:
        proxy = True
        verbose_name = 'Story / Article'
        verbose_name_plural = 'Stories & Articles'

class DiscoverPage(PageContent):
    class Meta:
        proxy = True
        verbose_name = 'Discover Page'
        verbose_name_plural = 'Discover Pages'

class ValuePage(PageContent):
    class Meta:
        proxy = True
        verbose_name = 'Value Page'
        verbose_name_plural = 'Value Pages'

class UtilityContact(ContactMessage):
    class Meta:
        proxy = True
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'

class UtilityPage(PageContent):
    class Meta:
        proxy = True
        verbose_name = 'Utility Page'
        verbose_name_plural = 'Utility Pages'
