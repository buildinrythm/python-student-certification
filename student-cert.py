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

def printCertificate(candidateName, certificationName, modules, results, average, overallOutcome):
    print("\n==============================================")
    print("             CERTIFICATION RESULT")
    print("==============================================")
    print(f"Candidate Name : {candidateName}")
    print(f"Certification  : {certificationName}\n")

    # Table header
    print(f"{'Module':20} {'Result':>6} {'Grade':>7} {'Outcome':>10}")
    print("-" * 45)

    # Table rows
    for i in range(len(modules)):
        grade, outcome = getGradeAndOutcome(results[i])
        print(
            f"{modules[i]:20} "
            f"{results[i]:>6}% "
            f"{grade:>7} "
            f"{outcome:>10}"
        )

    print("-" * 45)
    print(f"{'Overall Average':20} {average:>6.2f}%")
    print(f"{'Final Result':20} {overallOutcome}")
    print("==============================================\n")

def main():
    display_welcome()

    run_again = "Y"
    while run_again.upper() == "Y":
        process_candidate()
        run_again = input("Enter results for another candidate [Y/N]? ")

    print("\nSystem exiting. Goodbye!")


main()