import csv

from student import Student


def save_to_csv(students: list[Student], filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "email", "score"])

        for student in students:
            writer.writerow([student.name, student.age, student.email, student.score])
