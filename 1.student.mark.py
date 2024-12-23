def input_numberOfStudents():
    return int(input("Enter the number of students: "))

def input_studentInfo(numStu):
    students = []
    for i in range(numStu):
        studentId = input(f"Enter ID for student {i+1}: ")
        name = input(f"Enter name of student {i+1}:")
        dob = input(f"Enter date of birth for student {i+1} (DD/MM/YYYY): ")
        students.append((studentId, name, dob))
    return students
    
def input_numberOfCourses():
    return int(input("Enter the number of courses: "))

def input_courseInfo(numCourses):
    courses = []
    for j in range (numCourses):
        courseId = input(f"Enter ID for course {j+1}:")
        courseName = input(f"Enter name for course {j+1}:")
        courses.append((courseId, courseName))
    return courses

def input_marks(students, courses):
    marks = {}
    courseId = input("Enter course Id to input mark: ")
    if courseId not in [course[0] for course in courses]:
        print("Course not found!\n")
        return marks
    print(f"Input marks for courses{courseId}\n")
    for student in students: 
        mark = float(input(f"Enter mark for student {student[1]} (ID: {student[0]}):"))
        marks[student[0]] = mark
    return {courseId: marks}
    
def listCourses (courses):
    print("List of courses:\n")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def listStudents(students):
    print("List of students:")
    for student in students: 
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def showMarks(marks, courseId):
    if courseId not in marks:
        print("No marks available for this course!\n")
        return
    print(f"Marks for Course {courseId}:\n ")
    for studentId, mark in marks[courseId].items():
        print(f"Student Id: {studentId}, Mark: {mark}")


def main():
    students = []
    courses = []
    marks = {}

    while True: 
        print("--- Student Mark Management System ---\n")
        print("1. Input number of students and their information")
        print("2. Input number of courses and their information")
        print("3. Input marks for a course")
        print("4. List all students")
        print("5. List all courses")
        print("6. Show student marks for a course")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            numStu = input_numberOfStudents()
            students = input_studentInfo(numStu)
        elif choice == '2':
            numCourses = input_numberOfCourses()
            courses = input_courseInfo(numCourses)
        elif choice == '3':
            new_marks = input_marks(students, courses)
            marks.update(new_marks)
        elif choice == '4':
            listStudents(students)
        elif choice == '5':
            listCourses(courses)
        elif choice == '6':
            course_id = input("Enter course ID to show marks: ")
            showMarks(marks, course_id)
        elif choice == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()