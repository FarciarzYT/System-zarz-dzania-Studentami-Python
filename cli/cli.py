from utils.helper import clear_console
def menu():
        print(" ")
        print("Student Managment System")
        print("1 : Show all students")
        print("2 : Show Best Student")
        print("3 : Manage Students")
        print("4 : Add Student")
        print("5 : Delete Student")
        print("l : LoadStudents")
        print("q : Quit")
        print("")

def save_changes(manager):
        save = input("Do you want to save the changes to the file? (y/n): ")
        if save.lower == "y":
                manager.save_students()
        else:
                clear_console()
                return

