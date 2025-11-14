from sphinxawesome_theme.postprocess import Icons

project = 'Judge0 Docs'
copyright = '2025, Judge0 d.o.o.'
author = 'Judge0 d.o.o.'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_title = project
html_theme = 'sphinxawesome_theme'
html_permalinks_icon = Icons.permalinks_icon
html_static_path = ['_static']
html_show_sphinx = False
