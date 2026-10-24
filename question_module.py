
def generate_follow_up_questions(patient_data, missing_info):
    questions = []

    symptoms = patient_data["symptoms"].lower()

    if any(word in symptoms for word in ["fever", "temperature"]):
        questions.append(
            "What is your measured body temperature?"
        )

    if not patient_data["duration"].strip():
        questions.append(
            "When did the symptoms begin?"
        )

    if any(word in symptoms for word in ["cough", "breathing"]):
        questions.append(
            "Are you experiencing difficulty breathing?"
        )

    if "cough" in symptoms:
        questions.append(
            "Is your cough dry or producing mucus?"
        )

    questions.append(
        "Are your symptoms improving or worsening?"
    )

    questions.append(
        "Have you developed any additional symptoms?"
    )

    questions.append(
        "Do you have any relevant medical conditions or allergies?"
    )

    return questions
