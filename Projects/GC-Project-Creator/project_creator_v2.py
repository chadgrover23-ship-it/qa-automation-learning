from pathlib import Path
import shutil


BASE_FOLDER = Path(__file__).parent

OUTPUT_FOLDER = BASE_FOLDER / "test_output"
TEMPLATE_SOURCE = BASE_FOLDER / "templates" / "test_template.txt"



def create_instrument_project(serial_number):
    serial_number = serial_number.strip()


    if not serial_number:
        return False, "A serial number is required."
    
    project_folder = OUTPUT_FOLDER / serial_number
    customer_folder = project_folder / "Customer Folder"
    template_destination = project_folder / "test_template.txt"


    if project_folder.exists():
        return False, f"A folder already exists for serial number {serial_number}."
    
    if not TEMPLATE_SOURCE.exists():
        return False, "The template file could not be found."
    
    project_folder.mkdir(parents=True)
    customer_folder.mkdir()

    shutil.copy2(TEMPLATE_SOURCE, template_destination)

    return True, f"Project created successfully for serial number {serial_number}."


print("GC Test Project Creator V2.0")
print("-----------------------------")

entered_serial_number = input("Enter Serial Number: ")

success, message = create_instrument_project(entered_serial_number)


print()
print(message)
    