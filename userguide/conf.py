# -*- coding: utf-8 -*-

# requirements:
# textproc/py-sphinx
# textproc/py-sphinx_numfig
# textproc/py-sphinx_rtd_theme
# textproc/py-sphinxcontrib-httpdomain

import sys, os

templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# General information about the project.
copyright = u'2011-2016, iXsystems'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '9.10.2'
# The full version, including alpha/beta/rc tags.
release = '9.10.2'

# exclude_patterns is a list of patterns relative to the source directory
# that match files and directories to ignore when looking for source files.
tags.add('zfstor')
brand = u'ZFStor'
project = brand + u' User Guide'
master_doc = 'zfstor'
extensions = [
    'sphinx.ext.ifconfig',
    'sphinxcontrib.httpdomain'
]
numfig = True
numfig_secnum_depth = (2)

if tags.has('truenas'):
    brand = u'TrueNAS®'
    tags.remove('freenas')
    project = brand + u' User Guide'
    version = '9.10.1-U2.1'
    release = '9.10.1-U2.1'
    master_doc = 'truenas'

# |brand| will be replaced with FreeNAS® or TrueNAS®
# rst_epilog = '.. |brand| replace:: %s' % brand


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Option to change :menuselection: arrow -----------------------------

from docutils import nodes, utils
from docutils.parsers.rst import roles
from sphinx.roles import _amp_re

def patched_menusel_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    if typ == 'menuselection':
        text = text.replace('-->', u'\u2192') # Here is the patch

    spans = _amp_re.split(text)

    node = nodes.literal(rawtext=rawtext)
    for i, span in enumerate(spans):
        span = span.replace('&&', '&')
        if i == 0:
            if len(span) > 0:
                textnode = nodes.Text(span)
                node += textnode
            continue
        accel_node = nodes.inline()
        letter_node = nodes.Text(span[0])
        accel_node += letter_node
        accel_node['classes'].append('accelerator')
        node += accel_node
        textnode = nodes.Text(span[1:])
        node += textnode

    node['classes'].append(typ)
    return [node], []

# Use 'patched_menusel_role' function for processing the 'menuselection' role
roles.register_local_role("menuselection", patched_menusel_role)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'trueos_style'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "stickysidebar": "true"
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_static/themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = brand + ' User Guide ' + version + ' Table of Contents'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "artwork/freenaslogo.png"
if tags.has('truenas'):
    html_logo = "artwork/truenaslogo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "artwork/freenas.ico"
if tags.has('truenas'):
    html_favicon = "artwork/truenas.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'FreeNASdoc'
if tags.has('truenas'):
    htmlhelp_basename = 'TrueNASdoc'

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'FreeNAS® User Guide'
if tags.has('truenas'):
    epub_title = u'TrueNAS® User Guide'
epub_author = u'iXsystems'
epub_publisher = u'iXsystems'
epub_copyright = u'2011-2016, iXsystems'

# The basename for the epub file. It defaults to the project name.
epub_basename = u'zfstor_userguide'
if tags.has('truenas'):
    epub_basename = u'truenas_userguide'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'URL'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'zfstor.org'

# A unique identification for the text.
epub_uid = release

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
epub_show_urls = 'no'

# If false, no index is generated.
#epub_use_index = True


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': '\usepackage{array,ragged2e}',

# remove blank pages
'classoptions': ',openany',
'babel': '\\usepackage[english]{babel}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('zfstor', 'ZFStor.tex', u'ZFStor Documentation',
   u'ZFStor', 'manual'),
]

if tags.has('truenas'):
    latex_documents = [
      ('truenas', 'TrueNAS.tex', u'TrueNAS Documentation',
       u'iXsystems', 'manual'),
    ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'zfstor', u'ZFStor Documentation',
     [u'ZFStor'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'FreeNAS', u'FreeNAS Documentation',
   u'iXsystems', 'FreeNAS', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'
