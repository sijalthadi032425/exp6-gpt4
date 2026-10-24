
import ollama


def extract_symptoms(symptom_text):
    prompt = f"""
    Extract only the symptoms explicitly mentioned by the user.

    Do not invent symptoms or medical details.
    Return the symptoms as a simple bullet list.

    User input:
    {symptom_text}
    """

    try:
        response = ollama.chat(
            model="llama3.2:latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={"temperature": 0}
        )

        return response["message"]["content"]

    except Exception as error:
        return f"Symptom extraction failed: {error}"
