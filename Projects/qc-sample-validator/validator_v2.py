print("QC Sample Validator V2")
print("---------------------")

sample_count = 0

keep_running = "Y"

sample_id = input("Enter Sample ID: ")
analyst = input("Enter Analyst Name: ")

while keep_running == "Y":

    sample_id = input("Enter Sample ID: ")
    
    

    result = float(input("Enter Result Value: "))
                   
    min_spec = 4.0
    max_spec = 6.0

    print()
    print("Sample Report")
    print("-----------------")
    print("Sample:", sample_id)
    print("Analyst:", analyst)
    print("Result:", result)

    if result < min_spec:
        print("Status: FAIL")
        print("Reason: Below minimum specification.")

    elif result > max_spec:
        print("Status: FAIL")
        print("Reason: Above maximum specification.")

    else:
        print("Status: PASS")

    print()

    sample_count = sample_count + 1

    keep_running = input("Test another sample? (Y/N): ").upper()


print()
print("Samples Tested:", sample_count)
print("Program Closed")