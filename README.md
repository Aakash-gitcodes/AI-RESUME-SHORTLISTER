# AI Resume Shortlister

An AI-powered Resume Screening and Shortlisting System built using Python.  
This project helps automate the recruitment process by extracting candidate details from resumes, matching skills with job requirements, and ranking candidates based on skill compatibility.

---

## 📌 Features

- Extracts text from PDF resumes
- Extracts candidate details:
  - Name
  - Email
  - Phone Number
- Matches candidate skills with required skills
- Calculates matching score
- Ranks candidates automatically
- Exports shortlisted candidates to CSV
- Handles multiple resumes efficiently

---

## 🛠 Technologies Used

- Python
- Pandas
- PyMuPDF (fitz)
- Regular Expressions (Regex)
- OS Module

---

## 📂 Project Structure

AI Project/
│
├── app.py
├── parser.py
├── matcher.py
├── skills.py
├── resume/
└── shortlisted_candidates.csv

---

## ⚙️ How It Works

1. Upload resumes into the `resume` folder
2. The system extracts text from PDF resumes
3. Candidate information is identified using regex
4. Skills are matched with predefined required skills
5. Candidates are ranked based on matching score
6. Results are exported into a CSV file

---

## ▶️ Installation

### Clone the Repository

git clone https://github.com/Aakash-gitcodes/AI-RESUME-SHORTLISTER.git
