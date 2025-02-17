import io
import docx
import fitz


def extract_from_pdf(file_content):
    text = ""
    pdf_document = fitz.open(stream=file_content, filetype="pdf")
    for page in pdf_document:
        text += page.get_text()
    return text

def extract_from_docx(file_content):
    doc = docx.Document(io.BytesIO(file_content))
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


async def extract_text_from_file(file):
    content = await file.read()
    if file.filename.lower().endswith(".docx"):
        return extract_from_docx(content)
    elif file.filename.lower().endswith(".pdf"):
        return extract_from_pdf(content)
    else:
        return "Unsupported file format"
