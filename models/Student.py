class Student:
    student_count = 1
    def __init__(self,name, surname,group, grades , presence):
        self.id = Student.student_count
        self.name = name
        self.surname = surname
        self.group = group if isinstance(group, str) else "None"
        self.grades = grades if isinstance(grades, list) else []
        self.presence = presence if 100 >= presence >= 0 else 0
        Student.student_count += 1

   #metody wymagane do zapisu do json
    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "group": self.group,
            "grades": self.grades,
            "presence": self.presence
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            surname=data["surname"],
            group=data["group"],
            grades=data.get("grades", []),
            presence=data.get("presence", 0)
        )

    def __str__(self):
        return f" id: {self.id} | name:{self.name} | surname: {self.surname} | group: {self.group} | grades: {self.grades} | avg: {self.average_grade():.2f} | presence: {self.presence}% | "


    def average_grade(self):
        valid_grades = [g for g in self.grades if isinstance(g, (int, float))]
        if not valid_grades:
            return 0.0
        return sum(valid_grades) / len(valid_grades)











