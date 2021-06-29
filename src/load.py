# ---- * ---- * ---- * ---- Load the data from pdf files  ---- * ---- * ---- * ----

import pdfplumber
import pandas as pd


def load_pdf():
    """
    Load pdf file and return the extracted text
    """
    file_path = "/Users/user/hannahsophieMWB/Final Report on Guidelines on revised ML TF Risk Factors.pdf"
    # Get the total number of pages
    with pdfplumber.open(file_path) as pdf:
        totalpages = len(pdf.pages)
        text = []
        all_pages = []
        for page in range(totalpages):
            test = pdf.pages[page]  # replace the number 54 with "page" once the regex are fixed
            test_text = test.extract_text()
            all_pages.append(page)
            text.append(test_text)
        df = pd.DataFrame(all_pages, text).reset_index()
        df.columns = ["text", "page"]
        return df
