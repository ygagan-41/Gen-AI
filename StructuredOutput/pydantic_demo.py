from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr

new_student = {"name":"manny","age":19,"email":"abc@gmail.com"}

Student = Student(**new_student)

student_dict = dict(Student)

student_json = Student.model_dump_json()
