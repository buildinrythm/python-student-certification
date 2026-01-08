# ----------------------------------------
# Student Certification Processing System
# ----------------------------------------

def displayWelcome():
    print("======================================")
    print(" Welcome to the Certification System ")
    print("======================================\n")


def getGradeAndOutcome(score):
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


def processCandidate():
    candidateName = input("Enter candidate name: ")
    certificationName = input("Enter certification name: ")

    moduleNames = [
        "Databases",
        "Programming",
        "Web Development",
        "Networking",
        "Systems Analysis"
    ]

    moduleResults = []
    totalScore = 0

    print("\nEnter module results:")

    for module in moduleNames:
        score = int(input(f"{module} result: "))
        moduleResults.append(score)
        totalScore += score

    average = totalScore / len(moduleNames)

    if average >= 50:
        overallOutcome = "PASS"
    else:
        overallOutcome = "FAIL"

    printCertificate(
        candidateName,
        certificationName,
        moduleNames,
        moduleResults,
        average,
        overallOutcome
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
    displayWelcome()

    runAgain = "Y"
    while runAgain.upper() == "Y":
        processCandidate()
        runAgain = input("Enter results for another candidate [Y/N]? ")

    print("\nSystem exiting. Goodbye!")


main()
