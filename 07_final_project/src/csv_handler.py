import csv

from student import Student

FIELD_NAMES: list[str] = ["name", "age", "email", "score"]


def save_to_csv(students: list[Student], filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(FIELD_NAMES)

        for student in students:
            writer.writerow([student.name, student.age, student.email, student.score])


def load_from_csv(filename: str) -> list[Student]:
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        students: list[Student] = []

        for row in reader:
            students.append(
                Student(row["name"], int(row["age"]), row["email"], float(row["score"]))
            )

        return students
