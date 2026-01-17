import pdfplumber

def parse_resume(state):
    file_path = state['resume_path']

    text = ''
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return{'resume_text': text}