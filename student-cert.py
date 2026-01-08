# ----------------------------------------
# Student Certification Processing System
# ----------------------------------------

def displayWelcome():
    try:
        print("======================================")
        print(" Welcome to the Certification System ")
        print("======================================\n")
    except Exception as error:
        print("ERR001: Failed to display welcome message.", error)


def getGradeAndOutcome(score):
    try:
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
    except Exception as error:
        print("ERR002: Grade calculation failed.", error)
        return "N/A", "Error"


def processCandidate():
    try:
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

        writeToCsv(
            candidateName,
            certificationName,
            moduleNames,
            moduleResults
        )


    except ValueError:
        print("ERR003: Invalid input. Numeric result expected.")
    except Exception as error:
        print("ERR004: Error processing candidate.", error)

def writeToCsv(candidateName, certificationName, modules, results):
    try:
        with open("certificationResults.csv", "a") as file:
            row = candidateName + "," + certificationName

            for i in range(len(modules)):
                row += f",{modules[i]},{results[i]}"

            file.write(row + "\n")
            print("File written successfully")

    except Exception as error:
        print("ERR007: Failed to write to CSV file.", error)



def printCertificate(candidateName, certificationName, modules, results, average, overallOutcome):
    try:
        print("\n==============================================")
        print("             CERTIFICATION RESULT")
        print("==============================================")
        print(f"Candidate Name : {candidateName}")
        print(f"Certification  : {certificationName}\n")

        print(f"{'Module':20} {'Result':>6} {'Grade':>7} {'Outcome':>10}")
        print("-" * 45)

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

    except Exception as error:
        print("ERR005: Failed to print certificate.", error)


def main():
    try:
        displayWelcome()

        runAgain = "Y"
        while runAgain.upper() == "Y":
            processCandidate()
            runAgain = input("Enter results for another candidate [Y/N]? ")

        print("\nSystem exiting. Goodbye!")

    except Exception as error:
        print("ERR006: Critical system failure.", error)


main()
