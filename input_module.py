
def collect_patient_input():
    print("\n--- Patient Information ---")

    age = input("Enter age: ")
    sex = input("Enter sex (optional): ")
    symptoms = input("Describe your symptoms: ")
    duration = input("How long have you had these symptoms? ")
    severity = input("Severity (mild/moderate/severe): ")
    history = input("Relevant medical history (optional): ")
    medications = input("Current medications (optional): ")
    allergies = input("Known allergies (optional): ")

    patient_data = {
        "age": age,
        "sex": sex,
        "symptoms": symptoms,
        "duration": duration,
        "severity": severity,
        "history": history,
        "medications": medications,
        "allergies": allergies
    }

    return patient_data

def collect_patient_input():
    print("\n--- Patient Information ---")

    age = input("Enter age: ").strip()
    sex = input("Enter sex (optional): ").strip()
    symptoms = input("Describe your symptoms: ").strip()

    duration = input(
        "How long have you had these symptoms? (e.g., 2 days): "
    ).strip()

    severity = input(
        "Severity (mild/moderate/severe): "
    ).strip()

    history = input(
        "Relevant medical history (optional): "
    ).strip()

    medications = input(
        "Current medications (press Enter if none): "
    ).strip()

    allergies = input(
        "Known allergies (press Enter if none): "
    ).strip()

    def optional_value(value):
        if value.lower() in ("", "none", "n/a", "not applicable"):
            return ""
        return value

    patient_data = {
        "age": age,
        "sex": sex,
        "symptoms": symptoms,
        "duration": duration,
        "severity": severity,
        "history": optional_value(history),
        "medications": optional_value(medications),
        "allergies": optional_value(allergies)
    }

    return patient_data
