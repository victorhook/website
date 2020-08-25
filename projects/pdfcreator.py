from weasyprint import HTML

from urllib.request import urlopen
import os
import re


class PdfCreator:

    # Tags to limit the pdf-content from the html
    START_TAG = r'project-content">'
    END_TAG = r'<div class="row" id="download-btn">'
    REGEX = re.compile(r'(?<=%s).*?(?=%s)' % (START_TAG, END_TAG),
                       flags=re.DOTALL)

    @staticmethod
    def create_pdf(html, save_path):
        html = PdfCreator.REGEX.search(html).group(0)
        dir_path = os.path.dirname(save_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        HTML(string=html).write_pdf(save_path)
        with open(save_path, 'rb') as f:
            return f.read()
