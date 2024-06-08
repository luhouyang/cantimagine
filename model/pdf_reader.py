import pdfplumber


def extract_data(pdf_files):
    all_texts = []
    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as pdf:
            pdf_text = ''
            for page in pdf.pages:
                # Extract text, append if text is not None
                pdf_text += page.extract_text() or ''
            all_texts.append(pdf_text)
    return all_texts
