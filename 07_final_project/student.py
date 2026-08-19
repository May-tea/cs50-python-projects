class Student:
    def __init__(self, name: str, age: int, email: str, score: float) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.score = score

    def __str__(self) -> str:
        return f"Name: {self.name} | Age: {self.age} | Email: {self.email} | Score: {self.score}"
