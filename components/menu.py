from components.students import addStudents, viewAllStudents, removeStudent, updateStudent
from components.courses import addCourse,removeCourse,addStudentToCourse, updateCourseGrade, updateCourse
from components.viewCourses import viewCourses
from components.shared import sm 



def closeProgram():
    print("Saving data and exiting...")
    sm.save_data()
    print("Data saved. Program Terminated!")
    exit()


def pressEnterToContinue():
    input("\nPress Enter to continue...")
    

listMenu = [
    {"name":"Add student", "func":addStudents},
    {"name":"View all students", "func": viewAllStudents},
    {"name": "Remove student", "func": removeStudent},
    # {"name": "Update student", "func": updateStudent},
    {"name": "Add course","func": addCourse},
    {"name": "View courses", "func": viewCourses},
    {"name": "Update courses", "func": updateCourse},
    {"name": "Remove course", "func": removeCourse},
    {"name": "Add Student to Course", "func": addStudentToCourse},
    {"name": "Update or Add Course Grade", "func": updateCourseGrade},
    {"name":"Exit", "func": closeProgram}
    ]



def showMenu():
    sm.load_data()
    print("****** CLASS SCOREBOARD ******")
    for index, item in enumerate(listMenu):
        print(f"{index + 1}). {item["name"]}")
        

def runFunction(selectMenu):
    if 1 <= selectMenu <= len(listMenu):
        listMenu[selectMenu - 1]["func"]()
    else:
        print("Invalid input. Please try again.")
    pressEnterToContinue()