import csv

class SchoolManager:
    def __init__(self, data_dir="./csvFile/"):
        self.data_dir = data_dir if data_dir.endswith("/") else data_dir + "/"
        self.students = {}
        self.courses = {}
        self.student_id = 0
        self.course_id = 0
        self.load_data()

    def load_data(self):
        self._load_students()
        self._load_courses()
        self._load_enrollments()

    def _load_students(self):
        try:
            with open(self.data_dir + "students.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    sid = int(row["id"])
                    self.students[sid] = {"name": row["name"]}
                if self.students:
                    self.student_id = max(self.students.keys()) + 1
        except FileNotFoundError:
            pass

    def _load_courses(self):
        try:
            with open(self.data_dir + "courses.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cid = int(row["id"])
                    self.courses[cid] = {"name": row["name"], "students": {}}
                if self.courses:
                    self.course_id = max(self.courses.keys()) + 1
        except FileNotFoundError:
            pass

    def _load_enrollments(self):
        try:
            with open(self.data_dir + "course_enrollments.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cid = int(row["course_id"])
                    sid = int(row["student_id"])
                    grade = row.get("grade")
                    grade = float(grade) if grade else None

                    if cid in self.courses:
                        self.courses[cid].setdefault("students", {})[sid] = {"grade": grade}
        except FileNotFoundError:
            pass

    def save_data(self):
        self.save_students()
        self.save_courses()
        self.save_enrollments()

    def save_students(self):
        with open(self.data_dir + "students.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name"])
            writer.writeheader()
            for sid, data in self.students.items():
                writer.writerow({"id": sid, "name": data["name"]})

    def save_courses(self):
        with open(self.data_dir + "courses.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name"])
            writer.writeheader()
            for cid, data in self.courses.items():
                writer.writerow({"id": cid, "name": data["name"]})

    def save_enrollments(self):
        with open(self.data_dir + "course_enrollments.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["course_id", "student_id", "grade"])
            writer.writeheader()
            for cid, course in self.courses.items():
                for sid, sinfo in course.get("students", {}).items():
                    grade = sinfo.get("grade")
                    writer.writerow({
                        "course_id": cid,
                        "student_id": sid,
                        "grade": "" if grade is None else grade
                    })
