
import ollama


def analyze_symptoms(prompt):
    try:
        response = ollama.chat(
            model="llama3.2:latest",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a cautious medical information assistant. "
                        "Provide general information, not a diagnosis. "
                        "Do not invent patient details or prescribe medication."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={"temperature": 0.2}
        )

        return response["message"]["content"]

    except Exception as error:
        return (
            "Analysis could not be generated. "
            "Please check whether Ollama is running. "
            f"Technical details: {error}"
        )
