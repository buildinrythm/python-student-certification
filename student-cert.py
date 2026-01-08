# ----------------------------------------
# Student Certification Processing System
# ----------------------------------------

def display_welcome():
    print("======================================")
    print(" Welcome to the Certification System ")
    print("======================================\n")

def get_grade_and_result(score):
    if 70 <= score <= 100:
        return "A", "Pass"
    elif 60 <= score <= 69:
        return "B", "Pass"
    elif 50 <= score <= 59:
        return "C", "Pass"
    elif 40 <= score <= 49:
        return "D", "Fail"
    else:
        return "E", "Fail"

def process_candidate():
    candidate_name = input("Enter candidate name: ")
    certification_name = input("Enter certification name: ")

    module_names = [
        "Databases",
        "Programming",
        "Web Development",
        "Networking",
        "Systems Analysis"
    ]

    module_results = []
    total_score = 0

    print("\nEnter module results:")

    for module in module_names:
        score = int(input(f"{module} result: "))
        module_results.append(score)
        total_score += score

    average = total_score / len(module_names)

    if average >= 50:
        overall_result = "PASS"
    else:
        overall_result = "FAIL"

    print_certificate(
        candidate_name,
        certification_name,
        module_names,
        module_results,
        average,
        overall_result
    )
