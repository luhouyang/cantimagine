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


def extract_individual_data(pdf_file):

    with pdfplumber.open(pdf_file) as pdf:
        pdf_text = ''
        for page in pdf.pages:
            # Extract text, append if text is not None
            pdf_text += page.extract_text() or ''
        return pdf_text


def formatText(pdfDatas):
    full_text = "Here are the datas extracted from PDFs for your reference:\n"
    for pdf in pdfDatas:
        full_text += f'File name: {pdf["name"]} Content: {pdf["content"]}'
    return full_text[:4096]
