from weasyprint import HTML, CSS

from django.conf import settings

import os
import re


class PdfCreator:

    # Tags to limit the pdf-content from the html
    START_TAG = r'project-content-inner">'
    END_TAG = r'<div class="row" id="download-btn">'
    REGEX = re.compile(r'(?<=%s).*?(?=%s)' % (START_TAG, END_TAG),
                       flags=re.DOTALL)

    @staticmethod
    def create_pdf(html, base_url, stylesheet, save_path):

        return

        # Find the html content we're interested in
        html = PdfCreator.REGEX.search(html).group(0)

        # Create dir if it doesn't exist
        dir_path = os.path.dirname(save_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Grab stylesheet from filesystem
        css = CSS(settings.STATIC_ROOT + stylesheet)
        html = HTML(string=html, base_url=base_url)

        html.write_pdf(save_path, stylesheets=[css, settings.BOOTSTRAP_CSS])

