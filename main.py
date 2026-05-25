import os
import pandas as pd

# Import functions
from parser import (
    extract_text,
    extract_name,
    extract_email,
    extract_phone
)

from matcher import match_skills
from skills import skills


# STEP 1: Create Empty Candidate List

candidates = []


# STEP 2: Folder Containing Resumes

resume_folder = "resume"


# STEP 3: Read Every Resume

for file in os.listdir(resume_folder):

    # Only read PDF files
    if file.endswith(".pdf"):

        print("\nProcessing:", file)

        # Create full file path
        file_path = os.path.join(
            resume_folder,
            file
        )


        # STEP 4: Extract Resume Text
        
        text = extract_text(file_path)


        # STEP 5: Extract Candidate Details
        
        name = extract_name(text)

        email = extract_email(text)

        phone = extract_phone(text)


        # STEP 6: Match Skills
        
        matched_skills = match_skills(text)


        # STEP 7: Calculate Resume Score
        
        score = (len(matched_skills)/ len(skills)) * 100


    
        # STEP 8: Store Candidate Data
        
        candidate = {

            "Name": name,

            "Email": email,

            "Phone": phone,

            "Matched Skills": ", ".join(matched_skills),

            "Score": round(score, 2)

        }

        candidates.append(candidate)


# STEP 9: Rank Candidates

candidates.sort(
    key=lambda x: x["Score"],
    reverse=True
)

# STEP 10: Print Final Output

print("\n\n===== FINAL RANKING =====")

for index, candidate in enumerate(candidates, start=1):

    print("\n---------------------")

    print("Rank:", index)

    print("Name:", candidate["Name"])

    print("Email:", candidate["Email"])

    print("Phone:", candidate["Phone"])

    print("Skills:", candidate["Matched Skills"])

    print("Score:", candidate["Score"])



# STEP 11: Export CSV

df = pd.DataFrame(candidates)

df.to_csv(
    "shortlisted_candidates.csv",
    index=False
)

print("\nCSV File Created Successfully!")