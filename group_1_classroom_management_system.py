# ============================================================
# IMAN ELEVATE BOOTCAMP 2026
# FINAL CAPSTONE PROJECT
# CLASSROOM MANAGEMENT SYSTEM
# File-Based Version
# ============================================================

FILE_NAME = "group_1_students.txt"


# ============================================================
# 1. CALCULATE AVERAGE
# ============================================================

def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average


# ============================================================
# 2. CALCULATE GRADE
# ============================================================

def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 65:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# ============================================================
# 3. CALCULATE STATUS
# ============================================================

def calculate_status(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# ============================================================
# 4. GET VALID SCORE
# ============================================================

def get_score(score_number):
    while True:
        score = float(input("Enter Score " + str(score_number) + " (0-100): "))

        if score >= 0 and score <= 100:
            return score
        else:
            print("Score must be between 0 and 100.")


# ============================================================
# 5. ADD STUDENT
# ============================================================

def add_student(students, student_ids):

    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    if student_id in student_ids:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    department = input("Enter Department: ").strip()

    score1 = get_score(1)
    score2 = get_score(2)
    score3 = get_score(3)

    scores = [score1, score2, score3]

    average = calculate_average(scores)
    grade = calculate_grade(average)
    status = calculate_status(average)

    student = {
        "id": student_id,
        "name": name,
        "department": department,
        "scores": scores,
        "average": average,
        "grade": grade,
        "status": status
    }

    students.append(student)
    student_ids.add(student_id)

    print("Student added successfully.")


# ============================================================
# 6. DISPLAY ALL STUDENTS
# ============================================================

def display_all_students(students):

    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No student records available.")
        return

    print("-" * 85)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Department':<15}"
        f"{'Average':<10}"
        f"{'Grade':<10}"
        f"{'Status':<10}"
    )

    print("-" * 85)

    for student in students:

        print(
            f"{student['id']:<10}"
            f"{student['name']:<20}"
            f"{student['department']:<15}"
            f"{student['average']:<10.2f}"
            f"{student['grade']:<10}"
            f"{student['status']:<10}"
        )

    print("-" * 85)


# ============================================================
# 7. SEARCH STUDENT
# ============================================================

def search_student(students):

    print("\n========== SEARCH STUDENT ==========")

    search_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == search_id:

            print("\nStudent Found")
            print("----------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("Scores:", student["scores"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            print("Status:", student["status"])

            return

    print("Student not found.")


# ============================================================
# 8. UPDATE STUDENT
# ============================================================

def update_student(students):

    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent found.")
            print("1. Update Department")
            print("2. Update Scores")
            print("3. Update Department and Scores")

            choice = input("Choose an option: ").strip()

            if choice == "1":

                new_department = input("Enter new Department: ").strip()
                student["department"] = new_department

                print("Department updated successfully.")

            elif choice == "2":

                score1 = get_score(1)
                score2 = get_score(2)
                score3 = get_score(3)

                student["scores"] = [score1, score2, score3]

                student["average"] = calculate_average(
                    student["scores"]
                )

                student["grade"] = calculate_grade(
                    student["average"]
                )

                student["status"] = calculate_status(
                    student["average"]
                )

                print("Scores updated successfully.")

            elif choice == "3":

                new_department = input(
                    "Enter new Department: "
                ).strip()

                score1 = get_score(1)
                score2 = get_score(2)
                score3 = get_score(3)

                student["department"] = new_department
                student["scores"] = [score1, score2, score3]

                student["average"] = calculate_average(
                    student["scores"]
                )

                student["grade"] = calculate_grade(
                    student["average"]
                )

                student["status"] = calculate_status(
                    student["average"]
                )

                print("Student information updated successfully.")

            else:
                print("Invalid option.")

            return

    print("Student not found.")


# ============================================================
# 9. DELETE STUDENT
# ============================================================

def delete_student(students, student_ids):

    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            students.remove(student)
            student_ids.remove(student_id)

            print("Student deleted successfully.")

            return

    print("Student not found.")


# ============================================================
# 10. DISPLAY CLASS SUMMARY
# ============================================================

def class_summary(students):

    print("\n========== CLASS SUMMARY ==========")

    if len(students) == 0:
        print("No student records available.")
        return

    total_students = len(students)

    total_average = 0
    pass_count = 0
    fail_count = 0
    highest_average = students[0]["average"]

    for student in students:

        total_average = total_average + student["average"]

        if student["status"] == "Pass":
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

        if student["average"] > highest_average:
            highest_average = student["average"]

    class_average = total_average / total_students

    print("Total Students:", total_students)
    print("Lowest Average:", round(class_average, 2))
    print("Highest Average:", round(highest_average, 2))
    print("Number of Pass:", pass_count)
    print("Number of Fail:", fail_count)


# ============================================================
# 11. SAVE STUDENTS TO FILE
# ============================================================

def save_to_file(students, filename):
    file = open(filename, "w")

    # 1. Main Title with Equal Signs
    title_line = f"{'=' * 10} ALL STUDENTS {'=' * 30}\n"
    file.write(title_line)

    # 2. Table Headers
    headers = (
        f"{'ID':<8}"
        f"{'Name':<15}"
        f"{'Department':<15}"
        f"{'Average':<10}"
        f"{'Grade':<8}"
        f"{'Status':<8}\n"
    )
    divider = "-" * 65 + "\n"

    file.write(headers)
    file.write(divider)

    # 3. Write Student Rows
    for student in students:
        row = (
            f"{student['id']:<8}"
            f"{student['name']:<15}"
            f"{student['department']:<15}"
            f"{student['average']:<10.2f}"
            f"{student['grade']:<8}"
            f"{student['status']:<8}\n"
        )
        file.write(row)

    # 4. Closing Divider
    file.write(divider)
    file.close()

    print("Student records saved successfully.") 


# ============================================================
# 12. LOAD STUDENTS FROM FILE
# ============================================================

def load_from_file(filename, student_ids):

    students = []

    file = open(filename, "a+")
    file.seek(0)

    lines = file.readlines()

    file.close()

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        parts = line.split("|")

        if len(parts) == 4:

            student_id = parts[0]
            name = parts[1]
            department = parts[2]

            score_parts = parts[3].split(",")

            scores = []

            for score in score_parts:
                scores.append(float(score))

            average = calculate_average(scores)
            grade = calculate_grade(average)
            status = calculate_status(average)

            student = {
                "id": student_id,
                "name": name,
                "department": department,
                "scores": scores,
                "average": average,
                "grade": grade,
                "status": status
            }

            students.append(student)
            student_ids.add(student_id)

    return students


# ============================================================
# 13. SAVE BEFORE EXITING
# ============================================================

def exit_program(students):

    save_to_file(students, FILE_NAME)

    print("\nThank you for using Classroom Management System.")
    print("Goodbye!")


# ============================================================
# 14. MAIN MENU
# ============================================================

def main_menu():

    students = []
    student_ids = set()

    # Load existing records
    students = load_from_file(FILE_NAME, student_ids)

    while True:

        print("\n")
        print("=" * 50)
        print("       CLASSROOM MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Display Class Summary")
        print("7. Save Student Records")
        print("8. Load Student Records")
        print("9. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_student(students, student_ids)

        elif choice == "2":

            search_student(students)

        elif choice == "3":

            update_student(students)

        elif choice == "4":

            delete_student(students, student_ids)

        elif choice == "5":

            display_all_students(students)

        elif choice == "6":

            class_summary(students)

        elif choice == "7":

            save_to_file(students, FILE_NAME)

        elif choice == "8":

            students = load_from_file(
                FILE_NAME,
                student_ids
            )

            print("Student records loaded successfully.")

        elif choice == "9":

            exit_program(students)
            break

        else:

            print("Invalid choice. Please choose 1-9.")


# ============================================================
# PROGRAM START
# ============================================================

main_menu()