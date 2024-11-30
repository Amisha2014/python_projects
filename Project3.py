



def register_student():
    name = input("enter a name of a student")
    age = input ("enter a age of a student")
    grade = input ("enter a grade of a student")

    student_register = {
        "name" : name,
        "Age" : age,
        "Grade": grade
    }

    return student_register

def display_student_list (student):
    for key, value in student.items():
        print (f"{key} : {value}")

def main ():
    student = register_student()
    display_student_list (student)

main ()
