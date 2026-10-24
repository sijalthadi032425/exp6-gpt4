
from input_module import collect_patient_input
from profile_module import create_patient_profile
from symptom_module import extract_symptoms
from context_module import identify_missing_information
from prompt_module import create_medical_prompt
from analysis_module import analyze_symptoms
from question_module import generate_follow_up_questions
from safety_module import provide_medical_guidance
from save_module import save_analysis
from utils import format_patient_information


DISCLAIMER = """
DISCLAIMER
----------
This AI-generated response is intended for educational
and informational purposes only.

It is not a medical diagnosis and does not replace advice
from a qualified healthcare professional.

For serious, worsening or urgent symptoms, seek
appropriate medical care.
"""


def main():
    while True:
        print("\n========================================")
        print(" AI-POWERED MEDICAL SYMPTOM ASSISTANT")
        print("========================================")
        print("1. Enter Patient Information")
        print("2. Analyze Symptoms")
        print("3. Generate Follow-up Questions")
        print("4. Display Possible Conditions")
        print("5. Display Medical Attention Guidance")
        print("6. Display Disclaimer")
        print("7. Save Report")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            patient_data = collect_patient_input()

            profile = create_patient_profile(patient_data)
            symptoms = extract_symptoms(
                patient_data["symptoms"]
            )
            missing_info = identify_missing_information(
                patient_data
            )

            prompt = create_medical_prompt(
                patient_data,
                profile,
                symptoms,
                missing_info
            )

            print("\nGenerating preliminary analysis...")
            analysis = analyze_symptoms(prompt)

            questions = generate_follow_up_questions(
                patient_data,
                missing_info
            )

            guidance = provide_medical_guidance()

            report = f"""
AI-POWERED MEDICAL SYMPTOM ASSISTANT
===================================

1. REPORTED SYMPTOMS
--------------------
{symptoms}

2. PATIENT INFORMATION
---------------------
{format_patient_information(patient_data)}

3. POSSIBLE CONDITIONS AND EXPLANATION
--------------------------------------
{analysis}

4. MISSING INFORMATION
---------------------
""" + "\n".join(
                f"- {item}" for item in missing_info
            ) + """

5. FOLLOW-UP QUESTIONS
----------------------
""" + "\n".join(
                f"{i + 1}. {question}"
                for i, question in enumerate(questions)
            ) + f"""

6. MEDICAL ATTENTION GUIDANCE
-----------------------------
{guidance}

7. DISCLAIMER
-------------
{DISCLAIMER}
"""

            print("\nAnalysis generated.")
            print("\n" + report)

        elif choice == "2":
            if "report" not in locals():
                print("Please enter patient information first.")
            else:
                print(report)

        elif choice == "3":
            if "questions" not in locals():
                print("Please enter patient information first.")
            else:
                print("\nFOLLOW-UP QUESTIONS")
                for i, question in enumerate(questions, 1):
                    print(f"{i}. {question}")

        elif choice == "4":
            if "analysis" not in locals():
                print("Please enter patient information first.")
            else:
                print(analysis)

        elif choice == "5":
            print(provide_medical_guidance())

        elif choice == "6":
            print(DISCLAIMER)

        elif choice == "7":
            if "report" not in locals():
                print("Please analyze patient information first.")
            else:
                try:
                    path = save_analysis(report)
                    print(f"Report saved successfully: {path}")
                except OSError as error:
                    print(f"Could not save report: {error}")

        elif choice == "8":
            print("Exiting Medical Symptom Assistant. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 to 8.")


if __name__ == "__main__":
    main()
