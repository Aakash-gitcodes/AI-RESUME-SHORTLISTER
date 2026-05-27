from skills import skills
import re

# FUNCTION: Match Skills

def match_skills(text):

    matched_skills = []

    # Convert to lowercase
    text = text.lower()

    # Normalize separators
    text = text.replace("-", " ")
    text = text.replace("/", " ")
    text = text.replace(",", " ")

    for skill in skills:

        skill_lower = skill.lower()

        # SPECIAL CASES
        
        # Exact C++
        if skill_lower == "c++":

            pattern = r'(?<!\w)c\+\+(?!\w)'

        # Exact C only
        elif skill_lower == "c":

            # Avoid matching C++ or C#
            pattern = r'(?<!\w)c(?![\w#+])'

        # Exact Java only
        elif skill_lower == "java":

            # Avoid matching JavaScript
            pattern = r'(?<!\w)java(?!script)(?!\w)'

        # General Skills
        else:

            pattern = r'(?<!\w)' + re.escape(skill_lower) + r'(?!\w)'

        # Search pattern
        if re.search(pattern, text):

            matched_skills.append(skill)

    return matched_skills