from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

new_person: person = {'name':'mikey','age':21}

print(new_person)