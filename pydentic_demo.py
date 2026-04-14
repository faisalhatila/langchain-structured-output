from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Faisal"
    age: Optional[int] = None
    email:EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

new_student = {"name":"Musa", 'age':1, 'email':'abc@gmail.com'}

student = Student(**new_student)

# print(type(student))
# print(student.name)
# print(student.model_dump())

student_dict = dict(student)
print(student_dict)
student_json = student.model_dump_json()
print(student_json)