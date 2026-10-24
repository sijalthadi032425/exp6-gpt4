
def create_medical_prompt(patient_data, profile, symptoms, missing_info):
    prompt = f"""
You are an AI medical information assistant.

Analyze the information carefully and provide general,
cautious, educational information only.

PATIENT INFORMATION:
{profile}

ORIGINAL SYMPTOMS:
{patient_data["symptoms"]}

EXTRACTED SYMPTOMS:
{symptoms}

DURATION:
{patient_data["duration"]}

SEVERITY:
{patient_data["severity"]}

MISSING INFORMATION:
{missing_info}

MEDICAL HISTORY:
{patient_data["medical_history"] or "Not provided"}

CURRENT MEDICATIONS:
{patient_data["medications"] or "Not provided"}

ALLERGIES:
{patient_data["allergies"] or "Not provided"}

INSTRUCTIONS:
1. List the reported symptoms.
2. Identify possible conditions, without diagnosing.
3. Explain briefly why these conditions may be relevant.
4. List missing information.
5. Generate useful follow-up questions.
6. Provide cautious medical attention guidance.
7. Never invent symptoms or patient details.
8. Do not prescribe medication or recommend changing
   existing medication.
9. Mention emergency warning signs when appropriate.
10. Clearly state that this is not a medical diagnosis.

Use these sections:
1. Reported Symptoms
2. Patient Information
3. Possible Conditions
4. Explanation
5. Missing Information
6. Follow-up Questions
7. Medical Attention Guidance
8. Disclaimer
"""
    return prompt
