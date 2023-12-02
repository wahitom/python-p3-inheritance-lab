#!/usr/bin/env python

from user import User

import random

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
class Teacher(User): 

    def __init__(self, first, last, knowledge):
        super().__init__(first, last)

        self.knowledge = knowledge 

    def teach(self):
        # for item in knowledge:
        #     self.minimum = minimum
        #     self.maximum = maximum
        #     item = random.randint(minimum, maximum)
        #     print(item)
        #     return item

        if self.knowledge:
            random_str = random.randint(3, len(self.knowledge) - 1)
            return self.knowledge[random_str]
        else:
            return 'No knowledge available'

teacher = Teacher("Miriam", "Maina", knowledge)
#print(teacher.knowledge)
print(teacher.first)

random_element = teacher.teach()
print(random_element)
