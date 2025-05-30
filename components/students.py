from components.shared import sm 


def addStudents():
    while True:
        inputName = input("Name of Student (press Enter to stop): ").strip()

        if not inputName:
            break  # Stop adding students

        # Validation: check for duplicate name (case-insensitive)
        if any(s["name"].lower() == inputName.lower() for s in sm.students.values()):
            print(f"Student '{inputName}' already exists. Please enter a different name.")
            continue

        # Add new student
        sm.students[sm.student_id] = {"name": inputName}
        print(f"Student '{inputName}' added successfully with ID {sm.student_id}.")
        sm.student_id += 1
    # Save students after adding
    sm.save_students()


def viewAllStudents():
    if not sm.students:
        print("No students to display.")
        return

    while True:
        print("\nView Options:")
        print("1) View all students")
        print("2) Filter by course ID")
        print("3) Filter by minimum grade")
        print("4) Filter by course ID and minimum grade")
        print("5) Back to main menu")
        choice = input("Select an option: ").strip()

        if choice == "5":
            break  # exit to main menu

        course_filter = None
        grade_filter = None

        if choice == "2" or choice == "4":
            course_input = input("Enter Course ID to filter: ").strip()
            if not course_input.isdigit() or int(course_input) not in sm.courses:
                print("Invalid Course ID.")
                continue
            course_filter = int(course_input)

        if choice == "3" or choice == "4":
            try:
                grade_filter = float(input("Enter minimum grade: ").strip())
            except ValueError:
                print("Invalid grade input.")
                continue

        print("\n*** Students ***")
        found = False
        for sid, info in sm.students.items():
            student_name = info.get("name", "Unknown")

            # Apply course/grade filters
            passes_filter = True

            if course_filter is not None:
                course_students = sm.courses[course_filter]["students"]
                if sid not in course_students:
                    passes_filter = False

            if passes_filter and grade_filter is not None:
                found_grade = False
                for c in sm.courses.values():
                    if sid in c["students"]:
                        grade = c["students"][sid].get("grade")
                        if grade is not None and grade >= grade_filter:
                            found_grade = True
                            break
                if not found_grade:
                    passes_filter = False

            if passes_filter:
                print(f"Student ID: {sid}, Name: {student_name}")
                found = True

        if not found:
            print("No students matched the filter.")
        input("\nPress Enter to continue...")
        


def viewStudents():
    if not sm.students:
        print("No students to display.")
        return

    print("\n   ******* All Students ********"   )
    
    student_lines = []
    for id, student_data in sm.students.items():
        line = f"{id} - {student_data['name']}"
        student_lines.append(line)

    # Number of rows per column
    rows_per_column = 5
    # Split the list into chunks of 5
    columns = [student_lines[i:i + rows_per_column] for i in range(0, len(student_lines), rows_per_column)]

    # Determine the number of rows needed (max length among columns)
    max_rows = max(len(col) for col in columns)

    # Print row by row
    for row in range(max_rows):
        row_items = []
        for col in columns:
            if row < len(col):
                row_items.append(f"{col[row]:<30}")  # Adjust spacing as needed
            else:
                row_items.append(" " * 30)
        print("".join(row_items))

    



def removeStudent():
    if not sm.students:
        print("No students to remove.")
        return
    
    viewStudents()
    student_id_input = input("\nEnter the Student ID to remove: ").strip()
    if not student_id_input.isdigit():
        print("Invalid input. Please enter a valid numeric ID.")
        return

    sid = int(student_id_input)

    if sid in sm.students:
        removed_student = sm.students.pop(sid)
        print(f"Student '{removed_student['name']}' (ID: {sid}) has been removed successfully.")

        # Remove the student from all enrolled courses
        for cid, cdata in sm.courses.items():
            if sid in cdata.get("students", {}):
                del cdata["students"][sid]
                print(f"Removed from course: {cdata['name']}")

        # Save the updated data
        sm.save_data()
        print("Changes saved successfully.")
    else:
        print(f"No student found with ID {sid}.")


def updateStudent():
    if not sm.students:
        print("No students to update.")
        return

    viewStudents()
    student_id_input = input("\nEnter the Student ID to update: ").strip()
    if not student_id_input.isdigit():
        print("Invalid input. Please enter a valid numeric ID.")
        return

    sid = int(student_id_input)

    if sid not in sm.students:
        print(f"No student found with ID {sid}.")
        return

    current_name = sm.students[sid]["name"]
    print(f"Current name: {current_name}")
    new_name = input("Enter new name for the student: ").strip()

    if not new_name:
        print("Name cannot be empty. Update cancelled.")
        return

    # Check for duplicate name (excluding current student)
    if any(s["name"].lower() == new_name.lower() for id, s in sm.students.items() if id != sid):
        print(f"Student with name '{new_name}' already exists.")
        return

    sm.students[sid]["name"] = new_name
    print(f"Student ID {sid} name updated from '{current_name}' to '{new_name}'.")

    sm.save_students()




