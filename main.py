
from models.StudentManager import StudentManager
from models.Student import Student
from cli.cli import menu,save_changes
from utils.helper import clear_console,cat

def main():
    clear_console()
    manager = StudentManager()
    manager.load_students()
    running = True
    while running:
        menu()
        choice = input("Select an option: ")
        match choice:
            case "1":
                try:
                    clear_console()
                    question = input("Would you like to sort by average grade? (y/n): ")
                    if question.lower() == "y":
                        manager.sort_by_average()
                        clear_console()
                        manager.show_students()
                    else:
                        manager.show_students()
                except Exception as e:
                    print(e)
            case "2":
                clear_console()
                manager.show_best_student()
            case "3":
                clear_console()
                print("YOU ARE UPDATING AN USER")
                print("")

                try:
                    id_input = int(input("Enter student ID: "))
                    if id_input <= 0 or id_input > len(manager.students) :
                        print("Invalid student ID")
                        return
                    data = input("Enter Data: ")
                    pairs = data.split(",")
                    dict_data = {}

                    for pair in pairs:
                        key, value = pair.split("=")
                        dict_data[key] = value

                    manager.update_student(id_input, **dict_data)
                except Exception as e:
                    print(e)

            case "4":
                clear_console()
                print("YOU ARE ADDING AN STUDENT")
                print(" ")
                try:
                    name_input = input("Student name: ")
                    surname_input = input("Student surname: ")
                    group_input = input("Student group: ")
                    grade_input = input("Student grades: ")
                    presence_input = input("Student presence: ")
                    presence = int(presence_input)
                    grades = [float(x.strip()) for x in grade_input.split(",")]


                    if isinstance(grades, list):
                        x = Student(name_input, surname_input, group_input, grades,  presence)
                        manager.add_student(x)
                        print(x)
                        save_changes(manager)
                except Exception as e:
                    print(f"Error: {e}")

            case "5":
                clear_console()
                print("YOU ARE NOW DELETING A STUDENT!")
                print()

                id_input = input("Student ID: ")

                try:
                    for x in id_input.split(","):
                        student_id = int(x.strip())
                        manager.delete_student(student_id)

                    save_changes(manager)
                    clear_console()
                except ValueError:
                    print("Student ID is invalid.")

            case "q":
                clear_console()
                running = False
                print("Thank you for using this program.")
                print("")
            case "l":
                clear_console()
                cat()
                print("Loading Students...")
                manager.load_students()
                print("Students loaded.")


            case _:
                print("Unknown choice")








if __name__ == "__main__":
    main()