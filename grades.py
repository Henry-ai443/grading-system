class Student:
    def __init__(self, name, subjects, scores):
        self.name = name
        self.subjects = subjects
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    
    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        
    def display_result(self):
        print(f"Student Name: {self.name}")
        for i in range(len(self.subjects)):
            print(f"{self.subjects[i]}:{self.scores[i]}")
            print(f"Average Score:{self.calculate_average():.2f}")
            print(f"Grade:{self.get_grade()}")
            print("-------------------------")

def main():
    students = []

    num_students = int(input("Entaer the number of students: "))
    for _ in range(num_students):
        name = input("Enter student name: ")
        num_subjects = int(input("Enter the number of subjects for {}:".format(name)))
        subjects = []
        scores = []
        for _ in range(num_subjects):
            subject = input("Enter subject name: ")
            score = float(input(f"Enter score for {subject}: "))
            subjects.append(subject)
            scores.append(score)
            students.append(Student(name, subjects, scores))

            for student in students:
                student.display_result()

if __name__ == "__main__":
    main()