#!/usr/bin/env python

class User:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def first_name(self):
        return self.first
    
    def last_name(self):
        return self.last
    
    def full_name(self):
        self.fullname = '{} {}'.format(self.first, self.last)
        return self.fullname 

user = User("Miriam", "Maina")
print(user.full_name())
print(user.first_name())