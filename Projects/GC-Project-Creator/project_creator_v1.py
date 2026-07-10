from pathlib import Path
import shutil

print("GC Test Project Creator")
print("-----------------------")

serial_number = input("Enter Serial Number: ").strip()

base_folder = Path(__file__).parent

project_folder = base_folder / "test_output" / serial_number
customer_folder = project_folder / "Customer Folder"

template_source = base_folder / "templates" / "test_template.txt"
template_destination = project_folder / "test_template.txt"

if not serial_number:
    print("Error: A serial number is required.")

elif project_folder.exists():
    print("No folders were created.")
    print("Reason: A folder already exists for serial number", serial_number)

elif not template_source.exists():
    print("Error: The template file could not be found.")

else:
    project_folder.mkdir(parents=True)
    folders = ["Customer Folder", "Raw Data", "Reports"]
    
    for folder in folders:
        (project_folder / folder).mkdir()

    shutil.copy2(template_source, template_destination)

    print()
    print("Project created succesfully.")
    print("Serial Number:", serial_number)
    print("Project Folder:", project_folder)
    print("Customer Folder:", customer_folder)
    print("Template Copied:", template_destination)

