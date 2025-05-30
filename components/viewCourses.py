from components.shared import sm 

students = sm.students
course = sm.courses

def honourRole(cid):
    print("**** \nHonour Roll ****")
    for sid, info in course[cid]['students'].items():
        grade = info.get("grade")
        if grade is not None and grade >= 90:
            print(f"{sid} - {students.get(sid, {}).get('name', 'Unknown')} - Grade: {grade}")

def statistics(cid):
    grades = [info['grade'] for info in course[cid]['students'].values() if info['grade'] is not None]
    if grades:
        print(f"\n***** Statistics for {course[cid]['name']}: ****")
        print(f"Total Students with Grades: {len(grades)}")
        print(f"Highest Grade: {max(grades)}")
        print(f"Lowest Grade: {min(grades)}")
        print(f"Average Grade: {round(sum(grades) / len(grades), 2)}")
    else:
        print("No grades available.")

def listStudentsInCourse(cid):
    print(f"\n***** Students in {course[cid]['name']}: *****")
    if course[cid]['students']:
        for sid in course[cid]['students']:
            print(f"{sid} - {students.get(sid, {}).get('name', 'Unknown')}")
    else:
        print("No student found")

def findStudentsAboveThreshold(cid):
    try:
        threshold = float(input("\nEnter grade threshold: "))
        if cid in course:
            found = False
            print("**** List of Students above Threshold ****")
            for sid, info in course[cid]["students"].items():
                grade = info.get("grade")
                if grade is not None and grade > threshold:
                    print(f"{sid} - {students.get(sid, 'Unknown')} - Grade: {grade}")
                    found = True
            if not found:
                print("No students above the threshold.")
        else:
            print("Course not found.")
    except ValueError:
        print("Invalid threshold input.")


def computeClassAverage(cid):
    print("\n**** Class Average ****")
    if cid in course:
        grades = [info["grade"] for info in course[cid]["students"].values() if info["grade"] is not None]
        if grades:
            avg = sum(grades) / len(grades)
            print(f"Class average for {cid}: {avg:.2f}")
        else:
            print("No grades available.")
    else:
        print("Course not found.")
        

def searchStudents(cid):
    if not course[cid]["students"]:
        print("No students in this course.")
        return
    search = input("Please input name of student: ").strip().lower()
    found = False
    for sid in course[cid]["students"]:
        student_info = students.get(sid)
        if student_info and search in student_info["name"].lower():
            grade = course[cid]["students"][sid].get("grade", "N/A")
            print("\n**** Student found ****")
            print(f"Student ID : {sid}")
            print(f"Name       : {student_info['name']}")
            print(f"Grade      : {grade}")
            found = True
    if not found:
        print("\nNo records found in this course.")


def viewCoursesV2():
    if not course:
        print("No courses available.")
        return

    print("\n*** Available Courses ***")
    for cid, cinfo in course.items():
        print(f"ID: {cid} | Name: {cinfo['name']}")
    print()

viewListMenu = [
    {"name": "Search student", "func": searchStudents},
    {"name": "List Students in Course", "func": listStudentsInCourse},
    {"name": "Find Students Above Grade Threshold", "func": findStudentsAboveThreshold},
    {"name": "Compute Class Average", "func": computeClassAverage},
    {"name":"Print honour roll","func": honourRole},
    {"name":"Display Statistics", "func": statistics},
    {"name":"Back", "func": None},
    ]


def showViewListMenu():
    for index, item in enumerate(viewListMenu):
        print(f"{index + 1}). {item['name']}")  # Fix: use single quotes inside f-string


def viewRunFunction(selectMenu, cid):
    selected_item = viewListMenu[selectMenu - 1]
    if selected_item["func"] is not None:
        selected_item["func"](cid)
        input("\nPress Enter to continue...")


def viewCourses():
    while True:
        viewCoursesV2()
        course_input = input("Enter Course ID to view options or press Enter to return to main menu: ").strip()
        if not course_input:
            break
        if not course_input.isdigit() or int(course_input) not in course:
            print("Invalid Course ID.")
            continue
        cid = int(course_input)
        while True:
            print(f"\n*** Options for Course: {course[cid]['name']} (ID: {cid}) ***")
            showViewListMenu()
            sub_choice = input("\nSelect an option: ").strip()
            if not sub_choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            sub_choice_int = int(sub_choice)
            if sub_choice_int == len(viewListMenu):  # If "Back to Main Menu" is selected
                break
            elif 1 <= sub_choice_int <= len(viewListMenu):
                viewRunFunction(selectMenu=sub_choice_int, cid=cid)
            else:
                print("Invalid choice.")




