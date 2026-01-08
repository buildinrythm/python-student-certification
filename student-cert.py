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