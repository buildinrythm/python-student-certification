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

def print_certificate(name, cert_name, modules, results, average, overall):
    print("\n======================================")
    print("        CERTIFICATION RESULT")
    print("======================================")
    print(f"Candidate Name: {name}")
    print(f"Certification: {cert_name}\n")

    print("Module Results:")
    for i in range(len(modules)):
        grade, result = get_grade_and_result(results[i])
        print(
            f"{modules[i]:20} "
            f"Score: {results[i]:3}% "
            f"Grade: {grade} "
            f"Result: {result}"
        )

    print(f"\nOverall Average: {float(average):.2f}%")
    print(f"Final Outcome: {overall}")
    print("======================================\n")
