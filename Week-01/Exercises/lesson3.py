def check_sample(sample_id, result, min_spec, max_spec):

    print("-----------")
    print("Sample:", sample_id)
    print("Result:", result)
    print("Expected Range:", min_spec, "-", max_spec)
    if min_spec <= result <= max_spec:
        print("Status: PASS") 
    else:
        print("Status: FAIL")

check_sample("A101", 5.2, 4.0, 6.0)
check_sample("A102", 7.4, 4.0, 6.0)
check_sample("A103", 3.5, 4.0, 6.0)
check_sample("A104", 4.8, 4.0, 6.0)