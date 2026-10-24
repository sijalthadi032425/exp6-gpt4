
def create_patient_profile(patient_data):
    profile = {
        "Age": patient_data["age"],
        "Sex": patient_data["sex"] or "Not provided",
        "Medical History": patient_data["history"] or "Not provided",
        "Current Medications": patient_data["medications"] or "Not provided",
        "Allergies": patient_data["allergies"] or "Not provided"
    }

    return profile
