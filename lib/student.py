#!/usr/bin/env python

from user import User
from teacher import Teacher 


knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Student(User):
    def __init__(self, first, last, teacher):
        super().__init__(first, last)
        self.knowledge = []
        self.teacher = teacher

    def learn(self, num_items=1):
        learned_strings = []
        for _ in range(num_items):
            string = self.teacher.teach()

            if string not in self.knowledge:
                self.knowledge.append(string)
                learned_strings.append(string)

        return learned_strings



teacher_1 = Teacher("Miriam", "Maina", knowledge)

student = Student("Anne", "Maina", teacher_1)


# Accessing the 'first' attribute of the Student instance
print(student.first)

# Checking the knowledge of the student after learning
print(student.knowledge)

print(student.learn())