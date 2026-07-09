stud = {}


def show_menu():
    print("\n---- Student Menu ----")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

# This helps to add a new student in the list
def add_stud(stud):
    Stud_id = int(input("Enter the Student's ID: "))
    Stud_name = input("Enter the Student Name: ")
    Stud_age = int(input("Enter the age of the Student: "))
    Stud_course = input("Enter the course of the student: ")
    Stud_marks = float(input("Enter Student's marks: "))
    
    Stud_id = input("Enter the Student's ID: ")
    
    if stud_id in stud:
        print("Student ID Already Exists.")
    
    else:
        stud[Stud_id] = {
            "Name": Stud_name,
            "Age": Stud_age,
            "Course": Stud_course,
            "Marks": Stud_marks
            }
    
    print("Student Added Successfully.")


# It helps to view the details of the students
def view_stud(stud):
    if len(stud) == 0:
        print("No student record found")
    else:
        for Stud_id, info in stud.items():
            print(f"\nID: {Stud_id}")
            print(f"Name: {info['Name']}")
            print(f"Age: {info['Age']}")
            print(f"Course: {info['Course']}")
            print(f"Marks: {info['Marks']}")
            print("-----------------------")


# It searches for a specific student
def search_stud(stud):
    Stud_id = int(input("Enter the Student's ID: "))
    if Stud_id in stud:
        info = stud[Stud_id]
        print(f"\nID: {Stud_id}")
        print(f"Name: {info['Name']}")
        print(f"Age: {info['Age']}")
        print(f"Course: {info['Course']}")
        print(f"Marks: {info['Marks']}")
    else:
        print("Student not found")


# It updates the details of students already stored 
def update_stud(stud):
    Stud_id = int(input("Enter the Student's ID: "))
    if Stud_id in stud:
        field = input("Enter the field to be updated (Name/Age/Course/Marks): ")
        
        if field in stud[Stud_id]:
            
            if field == "Age":
                stud[Stud_id][field] = int(input("Enter new Age: "))
            
            elif field == "Marks":
                stud[Stud_id][field] = float(input("Enter new Marks: "))
            
            else:
                stud[Stud_id][field] = input(f"Enter new {field}: ")
                
            print("Student Updated Successfully")
            
        else:
            print("Invalid field name.")
            
    else:
        print("Student Not Found")

# This deletes the Student details from the records
def del_stud(stud):
    Stud_id = int(input("Enter the Student's ID: "))
    
    if Stud_id in stud:
        del stud[Stud_id]
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")
        return False

# Main Program
while True:
    show_menu()
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_stud(stud)
    elif choice == 2:
        view_stud(stud)
    elif choice == 3:
        search_stud(stud)
    elif choice == 4:
        update_stud(stud)
    elif choice == 5:
        del_stud(stud)
    elif choice == 6:
        print("Thank You")
        break
    else:
        print("Invalid Choice!")
