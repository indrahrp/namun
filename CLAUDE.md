# Namun — Nana Happy Cats

## Permissions

Claude runs in **bypass permissions mode** for this project. All tool calls (Bash, Edit, Write, Read, etc.) execute without asking for confirmation. Configured in `.claude/settings.local.json` via `"defaultMode": "bypassPermissions"`.

Do not ask for confirmation before running commands, editing files, or making changes in this project.

---

## Project

Django website for **Nana Happy Cats** — a personal site celebrating Nana and her 10 rescue cats. Deployed on Railway.

**Working directory:** `catgallery/`  
**Run dev server:** `python manage.py runserver 8000`  
**Collect static:** `python manage.py collectstatic --noinput`

---

## Structure

```
catgallery/
├── catsite/          # Django project settings + URLs
├── cats/             # Main app — homepage, cat cards, gallery
│   ├── static/cats/
│   │   ├── css/nana.css       # Full design system CSS
│   │   ├── js/                # (reserved)
│   │   └── img/               # All cat photos (her.png, timothy.png, …)
│   ├── templates/cats/
│   │   ├── base.html          # Nav + footer (Nana Happy Cats brand)
│   │   ├── gallery.html       # Homepage: hero, strip, cats grid, gallery, love quote
│   │   └── cat_detail.html    # Individual cat page
│   ├── models.py              # Cat model (DB-backed, used for detail pages)
│   └── views.py               # CATS + GALLERY data lists, gallery() view
└── blog/             # Blog app (post list, detail, write)
```

---

## Design

**Theme:** Nana Happy Cats — warm hand-drawn aesthetic.  
**Colors:** cream `#FBF2E1`, pink `#D98C86`, amber `#F3C46F`, ink `#473527`.  
**Fonts:** Caveat (headings/display) + Nunito (body/UI) via Google Fonts.  
**CSS:** single file at `cats/static/cats/css/nana.css`.

---

## Cat & Gallery Data

The 10 cats and 12 gallery items are defined as Python lists in `cats/views.py` (`CATS` and `GALLERY`). Each cat dict has `name`, `img` (static path), `role`, and `blurb`. Images live in `cats/static/cats/img/`.

The `Cat` Django model still exists for the `/cats/<pk>/` detail pages.

---

## Deployment

Railway. Config in `railway.json`. Procfile starts gunicorn on port 8080.  
Static files served by WhiteNoise. Push to `main` to deploy.

**Domains:**
- Production: `https://nanamuntu.com` (custom domain, DNS → Railway)
- Railway default: `https://namun-production.up.railway.app`
