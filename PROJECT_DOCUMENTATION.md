# GOURME Mushroom Marketplace - Project Documentation

## 1. Project Overview
GOURME is a minimalist, premium e-commerce platform and educational resource for gourmet and medicinal mushrooms. The project is built using **Python (Django)** and **Vanilla CSS/Tailwind**, emphasizing a high-end "Science & Soul" aesthetic inspired by minimalist Nordic design.

---

## 2. Technical Architecture
The project follows a standard Django MVT (Model-View-Template) architecture:
- **Backend**: Django 5.x
- **Frontend**: Django Templates + Tailwind CSS + Vanilla JS
- **Database**: SQLite (Development) / Compatible with PostgreSQL
- **Rich Text**: Django-Summernote (WYSIWYG editor for blogs)
- **Media**: Local storage for images and videos

---

## 3. Data Models (Database Schema)

### 🛒 Shop & Products
- **`Product`**: Core product model (Name, Price, Category, Primary & Hover images).
- **`Category`**: Product collections (Title, Slug, Hero images, Branding colors).

### 📖 CMS & Storytelling (Discover)
- **`PageContent`**: Dynamic pages (Best Sellers, Recipes, etc.). Controls Hero banners, Headlines, and Body text.
- **`Article`**: Blog-style stories belonging to a page.
- **`ContentBlock`**: Modular pieces within an article (Heading, Paragraph, Image, Video, Quote, Divider) that can be reordered freely.

### ✉️ Communication
- **`ContactMessage`**: Stores visitor inquiries (Name, Phone, Email, Query) with timestamp and read status.

---

## 4. Key Systems & Logic

### 🚀 Dynamic Page System
Pages are served via a flexible slug-based route (`/page/<slug>/`).
- **Logic**: The view fetches the `PageContent` object by slug, then pulls any "Featured Products" or "Articles" associated with that specific slug.
- **Template**: `page_detail.html` dynamically adjusts its layout based on whether it's showing a product grid or a blog feed.

### ✍️ Storytelling Engine (Summernote)
The admin is equipped with a visual editor that allows the store owner to:
- Write long-form articles.
- Insert images and videos directly into the text.
- Format text (bold, italic, headings) without writing HTML.

### 📱 Contact & WhatsApp Integration
- **Form Submission**: Saves to database + triggers an email notification to the owner.
- **WhatsApp Share**: Upon successful form submission, the user is given a button to forward their inquiry to the owner's WhatsApp.
- **Admin Reply**: One-click "Reply on WhatsApp" button in the admin panel to start a chat with the customer instantly.

---

## 5. Admin Organization (The Control Center)
The Django Admin has been customized into 4 logical "Menu Groups" to match the website's navigation:

1.  **SHOP**: Products, Categories, and Shop-specific pages (Best Sellers, etc.).
2.  **DISCOVER**: Blog Articles and Story-specific pages (Recipes, Benefits, etc.).
3.  **VALUE**: Promotional and combo pages.
4.  **UTILITY**: Contact Inquiries and utility pages (Account, Shipping).

---

## 6. Data & File Locations
- **Codebase**: `F:\gm website\gourme_mushrooms`
- **Database**: `F:\gm website\gourme_mushrooms\db.sqlite3`
- **Static Files**: `F:\gm website\gourme_mushrooms\static` (CSS, JS)
- **Media Files**: `F:\gm website\gourme_mushrooms\media` (User-uploaded images/videos)
- **Templates**: `F:\gm website\gourme_mushrooms\templates`

---

## 7. Developer Notes
- **Virtual Environment**: Located at `F:\gm website\gourme_mushrooms\venv`
- **Settings**: Email notifications are configured in `core/settings.py`. Currently set to "Console Backend" for testing.
- **Admin Login**: Username: `Admin`, Password: (User defined)

---
*Last Updated: May 13, 2026*
