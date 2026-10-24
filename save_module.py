
import os


def save_analysis(report):
    output_folder = "outputs"
    output_file = os.path.join(
        output_folder, "medical_analysis.txt"
    )

    os.makedirs(output_folder, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report)

    return output_file
