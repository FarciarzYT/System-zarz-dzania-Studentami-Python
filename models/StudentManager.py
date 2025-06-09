from copyreg import constructor
from models.Student import Student
import json

#Student Manager Odpowiedzialny już za dodawanie zapisu Studentów do plików i manipulacją danych studentów
class StudentManager:
    def __init__(self):
        self.students = []
    #metoda sortujaca studentów
    def sort_by_average(self, descending=True):
        self.students.sort(key=lambda s: s.average_grade(), reverse=descending)

    #Wyświetla najlepszego student pod względem średniej
    def show_best_student(self):
        best = None
        highest_avg = 0
        highest_presence = 0
        for s in self.students:
            avg = s.average_grade()
            presence = s.presence
            if avg >= highest_avg:
                highest_avg = avg
                best = s
        if best:
            print()
            print(best)
            print()
        else:
            print("No students found.")
    #wyswietla studentów
    def show_students(self):
        for s in self.students:
            print(s)

    #Dodaje Obiekt Studenta do dict Students

    def add_student(self,student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print('Student must be an instance of Student')

    # Usuwa Studenta Po Id
    def delete_student(self, *student_ids):
        if not student_ids:
            print("No student IDs provided.")
            return

        for student_id in student_ids:
            if not isinstance(student_id,int) or isinstance(student_id, bool):
                print(f"Invalid ID: {student_id} (must be integer)")
                continue
            found = False
            for s in self.students:
                if s.id == student_id:
                    found = True
                    self.students.remove(s)
                    print(f"Deleted student ID {student_id}")
                    found = True
                    break
            if not found:
                print(f"No student found with ID {student_id}")
                return 0

    #metoda odpowiedzialna za zapisywanie studentów do pliku json
    def save_students(self):
        try:
            with open("./data/studentdata.json", "w") as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4) # type: ignore
        except FileNotFoundError:
            print("No students found.")

    #metoda odpowiedzialna za wczytywanie studentów z pliku json
    def load_students(self):
        Student.student_count = 1
        try:
            with open("./data/studentdata.json", "r") as file:
                data = json.load(file)
                self.students = [Student.from_dict(item) for item in data]


        except FileNotFoundError:
            print("File not found")
            self.students = []
    # Metoda pozwalająca dodać ocenę w przedziale od 1.0 do 6.0
    def add_grade(self,student_id,**kwargs):
        student = next((s for s in self.students if s.id == student_id), None)
        if not student:
            print("Student not found")
            return
        for key , value in kwargs.items():
            if hasattr(student,key):
                if key == "grades":
                    for grade in value:
                        if isinstance(grade, (int, float)) and 1.0 <= grade <= 6.0:
                            student.grades.append(grade)
                        else:
                            print(f"Invalid grade {grade}: must be a number between 1.0 and 6.0")
                else:
                    if isinstance(value, (int, float)) and 1.0 <= value <= 6.0:
                        student.grades.append(value)
                    else:
                        print("Grade must be a number between 1.0 and 6.0")


    #Sprawdza czy id studenta instnieje jeżeli tak sprawdza jaki atrybut podalimy  i kontynuje ustawiająć atrybut do klucza
    def update_student(self, student_id, **kwargs):
        student = next((s for s in self.students if s.id == student_id), None)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return
        for key, value in kwargs.items():
            if hasattr(student, key):
                if key == "presence":
                    if not isinstance(value, (int, float)) or not (0 <= value <= 100):
                        print(f"Invalid value for presence: {value} (must be between 0 and 100)")
                        continue
                if key == "grades":

                    if not isinstance(value, list) or not all(isinstance(g, (int, float)) for g in value):
                        print(f"Invalid value for grades: {value} (must be a list of numbers)")
                        continue
                setattr(student, key, value)
                print(f"Updated {key} for student ID {student_id}")
            else:
                print(f"Unknown attribute '{key}' — skipping.")



