
def format_patient_information(patient_data):
    return f"""
Age: {patient_data['age'] or 'Not provided'}
Sex: {patient_data['sex'] or 'Not provided'}
Symptoms: {patient_data['symptoms'] or 'Not provided'}
Duration: {patient_data['duration'] or 'Not provided'}
Severity: {patient_data['severity'] or 'Not provided'}
Medical History: {patient_data['history'] or 'Not provided'}
Current Medications: {patient_data['medications'] or 'Not provided'}
Allergies: {patient_data['allergies'] or 'Not provided'}
"""
