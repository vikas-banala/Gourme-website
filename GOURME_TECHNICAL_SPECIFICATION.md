# GOURME Marketplace: Technical Specification & System Manual

## 1. Executive Summary
GOURME is a premium, high-performance e-commerce and content management platform tailored for the gourmet mushroom industry. Designed with a minimalist, Scandinavian-inspired aesthetic, the system bridges the gap between a robust commercial storefront and a rich educational portal. Built on the **Django Framework**, the platform emphasizes modularity, ease of administration, and high-conversion user interactions.

---

## 2. Architecture & Tech Stack

### 2.1 Backend Framework
- **Engine**: Django 5.x (Python-based)
- **Architecture**: Model-View-Template (MVT)
- **Environment**: Isolated Python Virtual Environment (venv)

### 2.2 Database Layer
- **Standard**: SQLite (Optimized for low-latency read operations)
- **Extensibility**: Fully compatible with PostgreSQL/MySQL for high-scale production.

### 2.3 Frontend & Design System
- **Framework**: Tailwind CSS & Vanilla CSS
- **Interactions**: Vanilla JavaScript (optimized for performance)
- **Rich Text**: Django-Summernote (Integrated WYSIWYG Editor)

---

## 3. Core Functional Modules

### 3.1 Advanced CMS (Content Management System)
The platform features a "Page-as-a-Service" model where every URL is a dynamic entry in the database.
- **Dynamic Routing**: The `/page/<slug>/` pattern handles all non-product pages.
- **Storytelling Engine**: Supports interleaved media (Images, 16:9 Videos), rich text, and decorative elements (Quotes, Dividers).
- **Featured Associations**: Pages can be "Product-Aware," allowing administrators to attach specific product collections (Best Sellers, Offers) to any CMS page.

### 3.2 E-Commerce & Product Inventory
- **Dual-State Imagery**: Every product supports a primary "Studio" shot and a "Lifestyle" hover shot for interactive browsing.
- **Categorization**: Multi-level hierarchy with custom branding colors (Hex codes) defined per category.
- **Dynamic Grids**: Responsive, layout-aware product grids that adapt to mobile and desktop viewports.

### 3.3 Integrated Contact & Lead Management
- **Persistence**: 100% of inquiries are captured in a relational database table (`ContactMessage`).
- **Communication Workflows**:
    - **Email**: Immediate SMTP-based notifications to the owner.
    - **WhatsApp Web-Share**: One-tap forwarding of inquiry details to WhatsApp.
    - **Direct Reply**: Admin-side "Reply on WhatsApp" button with pre-filled message templates.

---

## 4. Admin Operation & Management

### 4.1 Categorized Control Center
The administration interface is logically segmented into four pillars:
1.  **SHOP**: High-level inventory management (Products, Categories, Shop-specific pages).
2.  **DISCOVER**: Content-focused storytelling (Articles, Educational pages).
3.  **VALUE**: Sales & Promotion management (Offers, Combos, Subscriptions).
4.  **UTILITY**: Back-office operations (Inquiries, Terms, Utility pages).

### 4.2 Rich Content Creation
Administrators can create complex blog posts without code knowledge:
- **Embedded Media**: Upload images directly or paste YouTube/Vimeo URLs.
- **Modular Blocks**: Use Inlines to build structured sections (Ingredients, Methods, Guides).

---

## 5. Security & Maintenance

### 5.1 Security Protocols
- **CSRF Protection**: Enabled on all forms (Contact, Admin).
- **Authentication**: PBKDF2 with a SHA256 hash for secure password storage.
- **Middleware**: XSS and Clickjacking protection active by default.

### 5.2 Backup & Recovery
- **Snapshot Location**: `F:\gm website\backups\`
- **Database Backup**: Standard SQLite file-copy snapshots.
- **Media Assets**: Organized by date in the `/media/` directory.

---

## 6. Directory Map & Data Logic
| Component | Path | Description |
| :--- | :--- | :--- |
| **Project Root** | `F:\gm website\gourme_mushrooms` | Main application folder |
| **Database** | `db.sqlite3` | Relational data storage |
| **Media Root** | `/media/` | Product & Article images/videos |
| **Static Root** | `/static/` | CSS, JS, and Brand Assets |
| **Logic Layer** | `/shop/views.py` | Controller for dynamic pages |
| **Data Models** | `/shop/models.py` | Schema definitions |

---
**GOURME Technical Team**
*Confidential Document - Internal Use Only*
