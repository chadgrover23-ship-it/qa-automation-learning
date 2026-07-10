print("QC Sample Validator")
print("------------------------")

sample_id = input("Enter Sample ID: ")
analyst = input("Enter Analyst Name: ")

result = float(input("Enter test result: "))
min_spec = float(input("Enter minimum specification: "))
max_spec = float(input("Enter maximum specification: "))

print()
print("Sample Report")
print("------------------------")
print("Sample ID:", sample_id)
print("Analyst:", analyst)
print("Result:", result)
print("Specification Range:", min_spec, "-", max_spec)

if result < min_spec:
    print("Status: FAIL")
    print("Reason: Result is below the minimum specification.")
elif result > max_spec:
    print("Status: FAIL")
    print("Reason: Result is above the maximum specifcation.")
else: 
    print("Status: PASS")


