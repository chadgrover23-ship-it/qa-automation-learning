sample_id = input("Enter sample ID:")
result = float(input("Enter Result:"))
min_spec = 4.0
max_spec = 6.0
analyst = input("Enter Analyst Name:")

print("Sample:", sample_id)
print("Result:", result)
print("Specification:", min_spec, "to", max_spec)
print("Analyst:", analyst)
print("Sample:", sample_id)
if result >= min_spec and result <= max_spec:
    print("Status: PASS")
else:
    print("Status: FAIL")
    