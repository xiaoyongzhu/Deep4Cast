
# -*- coding: utf-8 -*-
#

import sys
import os
import pytorch_sphinx_theme

sys.path.insert(0, os.path.abspath('../deep4cast/'))

extensions = ['sphinx.ext.autodoc', 'nbsphinx']
source_suffix = '.rst'
master_doc = 'index'
project = u'Deep4Cast'
copyright = u''
exclude_patterns = ['_build', '**.ipynb_checkpoints']
pygments_style = 'sphinx'
# html_theme = "pytorch_sphinx_theme"
html_theme = "sphinx_rtd_theme"
html_logo = "images/thumb.jpg"
html_theme_options = {
    'logo_only': True,
    "style_nav_header_background" : "#3176BB"
}
autoclass_content = "both"
