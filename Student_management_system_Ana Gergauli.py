# სტუდენტების მართვის სისტემა
# შექმენით კონსოლის აპლიკაცია, რომელიც წარმოადგენს სტუდენტის მართვის მარტივ სისტემას ობიექტზე ორიენტირებული პროგრამირების პრინციპების გამოყენებით. 
# სისტემამ მომხმარებელს უნდა მისცეს საშუალება განახორციელოს ძირითადი ოპერაციები, რომლებიც დაკავშირებულია სტუდენტის ინფორმაციასთან.
# თითოეულ სტუდენტს უნდა ჰქონდეს ისეთი ატრიბუტები, როგორიცაა სახელი, სიის ნომერი და შეფასება. 
# კონსოლის აპლიკაციის შემუშავება რომელიც მომხმარებელს მისცემს საშუალებას იურთიერთოს სტუდენტთა მართვის სისტემასთან.


# სტუდენტური კლასი შემდეგი ატრიბუტებით:
# Name Name (string) - სახელი, Roll Number (int) - სიის ნომერი, Grade (char) - შეფასება. 
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

# მენიუს სისტემა: ჩვენება შემდეგი პარამეტრებით: 
# o ახალი სტუდენტის დამატება
    def add_new_student(self, name, roll_number, grade):
        """Add a new student to the system."""
        new_student = Student(name, roll_number, grade)
        self.students.append(new_student)

# o ყველა სტუდენტის ნახვა
    def view_all_students(self):
        """View details of all students in the system."""
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

# o სტუდენტის ძებნა ნომრის მიხედვით                
    def search_student_by_number(self, roll_number):
        """Search for a student by roll number and display details."""
        found = False
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
                found = True
                break
        if not found:
            print("Student not found.")

# o მოსწავლის შეფასების განახლება
    def update_student_grade(self, roll_number, new_grade):
        """Update a student's grade."""
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("Grade updated successfully.")
                break
        else:
            print("Student not found, grade not updated.")


def main():
    # სტუდენტების მართვის სისტემა
    sms = StudentManagementSystem()

    while True:
        # მენიუს ჩვენება
        print("\nStudent Management System Menu:")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student by number")
        print("4. Update a student's assessment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # ახალი სტუდენტის დამატება
            name = input("Enter student's name: ")
            if not all(char.isalpha() or char.isspace() for char in name):
                print("Error: Name should contain only letters and spaces.")
                continue 
            
            roll_number_input = input("Enter student's roll number: ")
            if not roll_number_input.isdigit():
                print("Error: Roll number should contain only numbers.")
                continue  
            roll_number = int(roll_number_input)
            
            grade_input = input("Enter student's grade: ")
            if not grade_input.isdigit():
                print("Error: Grade should contain only numbers.")
                continue 
            grade = grade_input
            
            sms.add_student(name, roll_number, grade)

        elif choice == '2':
            # ყველა სტუდენტის ჩვენება
            sms.view_all_students()

        elif choice == '3':
            # ნომრის მიხედვით სტუდენტის ძიება
            roll_number_input = input("Enter roll number: ")
            if not roll_number_input.isdigit():
                print("Roll number should contain only numbers.")
                continue  
            roll_number = int(roll_number_input)
            sms.search_student_by_number(roll_number)

        elif choice == '4':
            # სტუდენტის შეფასების განახლება
            roll_number_input = input("Enter roll number of student to update grade: ")
            if not roll_number_input.isdigit():
                print("Roll number should contain only numbers.")
                continue  
            roll_number = int(roll_number_input)
            
            new_grade_input = input("Enter new grade: ")
            if not new_grade_input.isdigit():
                print("Grade should contain only numbers.")
                continue  
            new_grade = new_grade_input
            
            sms.update_student_grade(roll_number, new_grade)

        elif choice == '5':
            # გამოსვლა
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
