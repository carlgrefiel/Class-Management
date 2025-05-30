from components.shared import sm
from components.viewCourses import viewCoursesV2
from components.students import viewStudents

def addCourse():
    while True:
        new_course = input("Enter new course name (press Enter to stop): ").strip()
        if not new_course:
            break  # Stop adding courses
        # Check for duplicate course name (case-insensitive)
        if any(c["name"].lower() == new_course.lower() for c in sm.courses.values()):
            print(f"Course '{new_course}' already exists. Please enter a different name.")
            continue
        # Add new course
        sm.courses[sm.course_id] = {"name": new_course, "students": {}}
        print(f"Course '{new_course}' added successfully with ID {sm.course_id}.")
        sm.course_id += 1
        
    sm.save_courses()


def addStudentToCourse():
    try:
        viewCoursesV2()
        course_code = int(input("\nEnter course ID: ").strip())
        viewStudents()
        student_code = int(input("\nEnter student ID: ").strip())
    except ValueError:
        print("Please enter valid numeric IDs.")
        return

    if course_code not in sm.courses:
        print("Invalid course ID.")
        return

    if student_code not in sm.students:
        print("Invalid student ID.")
        return

    course_students = sm.courses[course_code].setdefault("students", {})
    if student_code in course_students:
        print("Student already enrolled in the course.")
        return

    course_students[student_code] = {"grade": None}
    print(f"Student ID {student_code} added to course '{sm.courses[course_code]['name']}' (ID {course_code}).")

    # Save after adding enrollment
    sm.save_enrollments()


def updateCourse():
    if not sm.courses:
        print("No courses available to update.")
        return

    viewCoursesV2()
    cid_input = input("Enter the Course ID to update: ").strip()
    if not cid_input.isdigit():
        print("Invalid input. Please enter a valid numeric ID.")
        return

    cid = int(cid_input)
    if cid not in sm.courses:
        print(f"No course found with ID {cid}.")
        return

    old_name = sm.courses[cid]["name"]
    new_name = input(f"Enter new name for course '{old_name}': ").strip()
    if not new_name:
        print("No course name entered. Operation cancelled.")
        return

    # Check for duplicate course name
    if any(c["name"].lower() == new_name.lower() for id, c in sm.courses.items() if id != cid):
        print(f"A course with the name '{new_name}' already exists.")
        return

    sm.courses[cid]["name"] = new_name
    print(f"Course ID {cid} updated successfully: '{old_name}' ➜ '{new_name}'")

    sm.save_courses()


def updateCourseGrade():
    try:
        viewCoursesV2()
        course_code = int(input("\nEnter course ID: ").strip())
        viewStudents()
        student_code = int(input("\nEnter student ID: ").strip())
    except ValueError:
        print("Please enter valid numeric IDs.")
        return

    if course_code not in sm.courses:
        print("Invalid course ID.")
        return

    if student_code not in sm.courses[course_code].get("students", {}):
        print("Student is not enrolled in the specified course.")
        return

    try:
        grade = float(input("Enter grade: ").strip())
    except ValueError:
        print("Invalid grade input. Please enter a number.")
        return

    sm.courses[course_code]["students"][student_code]["grade"] = grade
    print(f"Grade updated successfully for student ID {student_code} in course '{sm.courses[course_code]['name']}'.")

    sm.save_enrollments()


def removeCourse():
    if not sm.courses:
        print("No courses to remove.")
        return
    viewCoursesV2()
    cid_input = input("Enter the Course ID to remove: ").strip()
    if not cid_input.isdigit():
        print("Invalid input. Please enter a valid numeric ID.")
        return

    cid = int(cid_input)
    if cid not in sm.courses:
        print(f"No course found with ID {cid}.")
        return

    course_name = sm.courses[cid]["name"]
    sm.courses.pop(cid)
    print(f"Course '{course_name}' removed from the list.")

    # Remove course enrollments from all students
    for student in sm.students.values():
        if "scores" in student and course_name in student["scores"]:
            student["scores"].pop(course_name)
            if student["scores"]:
                student["average"] = round(sum(student["scores"].values()) / len(student["scores"]), 2)
            else:
                student["average"] = 0.0

    print(f"'{course_name}' also removed from all student records.")

    sm.save_data()

