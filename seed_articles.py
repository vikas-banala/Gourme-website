import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from shop.models import PageContent, Article, ContentBlock
from datetime import date

# Get the Mushroom Benefits page
benefits_page = PageContent.objects.get(slug='benefits')

# Create a sample article
article, created = Article.objects.get_or_create(
    slug='reishi-mushroom-complete-guide',
    defaults={
        'page': benefits_page,
        'title': 'The Complete Guide to Reishi Mushroom',
        'summary': 'Discover why Reishi has been called the "Mushroom of Immortality" for over 2,000 years and how modern science validates its traditional uses.',
        'published_date': date(2026, 5, 1),
        'is_published': True,
        'order': 1,
    }
)

if created:
    # Add content blocks
    ContentBlock.objects.create(
        article=article, block_type='heading', order=1,
        text_content='A Living Legend of Traditional Medicine'
    )
    ContentBlock.objects.create(
        article=article, block_type='paragraph', order=2,
        text_content='Reishi mushroom (Ganoderma lucidum) has been a cornerstone of traditional Chinese medicine for over two millennia. Known as "Lingzhi" in Chinese — meaning "divine mushroom" or "mushroom of immortality" — it was once reserved exclusively for emperors and royalty.\n\nIts distinctive kidney-shaped cap with a lacquered, reddish-brown surface makes it one of the most recognizable medicinal fungi in the world. But beyond its striking appearance lies a powerhouse of bioactive compounds that modern science is only beginning to fully understand.'
    )
    ContentBlock.objects.create(
        article=article, block_type='quote', order=3,
        text_content='Reishi is nature\'s most sophisticated adaptogen — a biological intelligence that helps the body find its own balance.'
    )
    ContentBlock.objects.create(
        article=article, block_type='heading', order=4,
        text_content='The Science Behind the Magic'
    )
    ContentBlock.objects.create(
        article=article, block_type='paragraph', order=5,
        text_content='Modern research has identified over 400 bioactive compounds in Reishi mushrooms, including:\n\n• Triterpenoids (ganoderic acids) — support liver function and have anti-inflammatory properties\n• Beta-glucans — powerful immune system modulators\n• Peptidoglycans — contribute to immune-enhancing effects\n• Polysaccharides — support cellular health and longevity\n\nOur dual-extraction process ensures maximum bioavailability of both water-soluble (beta-glucans) and alcohol-soluble (triterpenoids) compounds.'
    )
    ContentBlock.objects.create(
        article=article, block_type='divider', order=6
    )
    ContentBlock.objects.create(
        article=article, block_type='heading', order=7,
        text_content='How to Incorporate Reishi Into Your Routine'
    )
    ContentBlock.objects.create(
        article=article, block_type='paragraph', order=8,
        text_content='The most effective way to consume Reishi is through a concentrated extract, taken consistently over time. Unlike stimulants, Reishi works subtly — building resilience and balance over weeks and months.\n\nWe recommend starting with 1-2 grams of our dual-extracted powder in the evening, mixed into warm water, tea, or your favorite golden milk recipe. Many of our customers report deeper sleep within the first week and improved stress resilience within the first month.'
    )
    print(f"Created article: {article.title} with {article.blocks.count()} content blocks")
else:
    print(f"Article already exists: {article.title}")

# Also create a sample article for Recipes
recipes_page = PageContent.objects.get(slug='recipes')
recipe_article, created2 = Article.objects.get_or_create(
    slug='reishi-golden-milk-recipe',
    defaults={
        'page': recipes_page,
        'title': 'Reishi Golden Milk',
        'summary': 'A warming, anti-inflammatory evening elixir that combines the calming power of Reishi with turmeric and spices.',
        'published_date': date(2026, 5, 5),
        'is_published': True,
        'order': 1,
    }
)

if created2:
    ContentBlock.objects.create(
        article=recipe_article, block_type='paragraph', order=1,
        text_content='This recipe is our most-loved evening ritual at GOURME. The combination of Reishi\'s calming adaptogens with turmeric\'s anti-inflammatory curcumin creates a truly restorative beverage that prepares both body and mind for deep, nourishing sleep.'
    )
    ContentBlock.objects.create(
        article=recipe_article, block_type='heading', order=2,
        text_content='Ingredients'
    )
    ContentBlock.objects.create(
        article=recipe_article, block_type='paragraph', order=3,
        text_content='• 1 cup oat milk (or any plant milk)\n• 1 tsp GOURME Reishi extract powder\n• ½ tsp ground turmeric\n• ¼ tsp ground cinnamon\n• Pinch of black pepper (enhances curcumin absorption)\n• 1 tsp raw honey or maple syrup\n• ½ tsp coconut oil'
    )
    ContentBlock.objects.create(
        article=recipe_article, block_type='heading', order=4,
        text_content='Method'
    )
    ContentBlock.objects.create(
        article=recipe_article, block_type='paragraph', order=5,
        text_content='1. Gently warm the plant milk in a small saucepan over medium-low heat. Do not boil.\n\n2. Whisk in the Reishi extract, turmeric, cinnamon, and black pepper until fully combined.\n\n3. Add the coconut oil and stir until melted through.\n\n4. Remove from heat and let cool slightly. Stir in the honey.\n\n5. Pour into your favorite ceramic mug and enjoy 30 minutes before bedtime.'
    )
    ContentBlock.objects.create(
        article=recipe_article, block_type='quote', order=6,
        text_content='This golden milk has become my nightly ritual. I sleep deeper and wake up feeling genuinely refreshed. — A GOURME customer'
    )
    print(f"Created article: {recipe_article.title} with {recipe_article.blocks.count()} content blocks")
else:
    print(f"Article already exists: {recipe_article.title}")

print("\nDone! All sample articles created.")
