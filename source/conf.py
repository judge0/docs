from sphinxawesome_theme.postprocess import Icons

project = 'Judge0 Docs'
copyright = '2025, Judge0 d.o.o.'
author = 'Judge0 d.o.o.'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_title = project
html_theme = 'sphinxawesome_theme'
html_favicon = "./_static/Judge0 Icon 02 Rounded 1024x1024.png"
html_theme_options = {
    "logo_light": "./_static/Judge0 Icon 07 Rounded 1024x1024.png",
    "logo_dark": "./_static/Judge0 Icon 06 Rounded 1024x1024.png",
    "main_nav_links": {
        "Docs": "/index",
        "Products": "/products",
        "Pricing": "/products/judge0/pricing",
        "FAQ": "/faq",
    },
    "show_prev_next": True,
    "awesome_external_links": True,
    "breadcrumbs_separator": "•",
    "show_scrolltop": True,
}
html_permalinks_icon = Icons.permalinks_icon
html_static_path = ['_static']
html_show_sphinx = False
