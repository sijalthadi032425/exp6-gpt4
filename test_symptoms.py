
from symptom_module import extract_symptoms

text = "I have fever and cough for two days. My throat is also painful."

print("Original Input:")
print(text)

print("\nExtracted Symptoms:")
print(extract_symptoms(text))
