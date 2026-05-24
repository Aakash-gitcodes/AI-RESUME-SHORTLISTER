import fitz
import re


# -----------------------------------
# FUNCTION 1
# Extract text from PDF
# -----------------------------------

def extract_text(pdf_path):

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    return text


# -----------------------------------
# FUNCTION 2
# Extract Candidate Name
# -----------------------------------

def extract_name(text):

    invalid_words = [
        "executive summary",
        "summary",
        "profile",
        "education",
        "skills",
        "projects",
        "experience",
        "objective"
        "professional summary"
    ]

    lines = text.split("\n")

    for line in lines[:20]:

        line = line.strip()

        if not line:
            continue

        # Remove extra spaces
        line = re.sub(r'\s+', ' ', line)

        # Skip headings
        if line.lower() in invalid_words:
            continue

        # Allow uppercase names too
        if re.match(r'^[A-Za-z.\s]+$', line):

            words = line.split()

            # Most names have 2-4 words
            if 2 <= len(words) <= 4:

                return line.title()

    return "Name Not Found"


# -----------------------------------
# FUNCTION 3
# Extract Email
# -----------------------------------

def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -----------------------------------
# FUNCTION 4
# Extract Phone Number
# -----------------------------------

def extract_phone(text):

    pattern = r"\+?\d[\d\s\-]{8,15}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"