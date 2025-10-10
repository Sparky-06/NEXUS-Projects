import csv

class StudentManagementSystem:
    def __init__(self, filename="data.csv"):
        self.filename = filename
        # Create the file with headers if it doesn't exist
        with open(self.filename, "a+", newline="") as fp:
            fp.seek(0)
            if not fp.read().strip():
                writer = csv.writer(fp)
                writer.writerow(["Name", "Roll", "Marks"])

    

    
    def new_student(self, name, roll, marks):
        with open(self.filename, "a+", newline="") as fp:
            
            #To check for duplicate Roll numbers
            fp.seek(0)
            reader = csv.reader(fp)
            lst = []
            next(reader, None)
            
            for row in reader:
                lst.append(row[1])

            if roll not in lst:
                writer = csv.writer(fp)
                writer.writerow([name, roll, marks])
                print("New Student added successfully!!\n")
            else:
                print(f"Roll number {roll} already exists....")
    


    def all_data(self):
        with open(self.filename, "r", newline="") as fp:
            reader = csv.reader(fp)
            for row in reader:
                print(row)
    



    def avg_marks(self, roll):  #Getting Average marks of the student
        with open(self.filename, "r", newline="") as fp:
            reader = csv.reader(fp)
            for row in reader:
                if row and row[1] == str(roll):
                    lst = eval(row[2])
                    break
                
            avg = sum(lst)/len(lst)
            print(f"Average marks of {row[0]} roll number {row[1]} is:", avg)


print("-----------------------------------------------------Welcome to the Student Marks Management System!!-----------------------------------------------------")
#print("Welcome to the Student Marks Management System!!")
print("Let's get started!!\n")

while True:
    print("\n\n")
    print("__INTERACTIVE MENU__")
    print("Press 1 to enter Student records")
    print("Press 2 to see all records in the database")
    print("Press 3 to get average marks of a student")
    print("Press 4 to exit the system")



    choice = int(input("Enter your choice (1/2/3):"))
    if choice == 1:
        print("\n\n")
        name = input("Enter name of student:")
        roll = int(input("Enter roll number of student:"))
        number_of_subjects = int(input("Enter number of Subjects for student:"))
        marks = []
        print("Enter marks of all the subjects, on by one please.")

        for i in range(0,number_of_subjects):
            marks.append(int(input("Enter marks:")))
        StudentManagementSystem().new_student(name, roll, marks)
    
    elif choice == 2:
        print("\n\n")
        StudentManagementSystem().all_data()

    elif choice == 3:
        print("\n\n")
        roll = int(input("Enter roll number of student you wish to see average marks of:"))
        StudentManagementSystem().avg_marks(roll)
    
    elif choice == 4:
        print("\n\n")
        print("Thank you for using our system, good bye")
        quit()
    
    else:
        print("Enter valid input!")