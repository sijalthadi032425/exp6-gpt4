
def identify_missing_information(patient_data):
    missing = []

    symptoms = patient_data["symptoms"].lower()

    if not patient_data["age"].strip():
        missing.append("Age")

    if not patient_data["duration"].strip():
        missing.append("Duration of symptoms")

    if not patient_data["severity"].strip():
        missing.append("Symptom severity")

    if any(word in symptoms for word in ["fever", "temperature"]):
        missing.append("Exact measured temperature")

    if any(word in symptoms for word in ["cough", "breathing"]):
        missing.append("Whether breathing difficulty is present")

    missing.append("Whether symptoms are improving or worsening")
    missing.append("Any additional symptoms")

    if not missing:
        return ["No missing information identified"]

    return missing
