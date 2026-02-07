from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated
class My_model(BaseModel):
    name:Annotated[str,Field(max_length=50,title="give name of patient",description="name of the patient",examples=["Isha,Nitish"])]
    email:EmailStr
    linkedIn:AnyUrl
    age:int
    weight:Annotated[float,Field(strict=True,gt=1,lt=90,title="constraints are there",description="weight should be greater than 1 and less then 90")]
    allergies:Annotated[Optional[List[str]],Field(default=None,description="give allergies if patient is having any")] #way to make a field optional
    # allergies:Optional[List[str]]=Field(max_length=5)   #it does data validation that -> max elements can be 5 only inside the list
    contact:Dict[str,str]=Field(max_length=5)
    married:bool=False

def insert_data(model:My_model):
    print(model.name)
    print(model.email)
    print(model.age)
    print(model.contact)
    print(model.allergies)
    print(model.married)
    print("inserted to DB")

def update_data(model:My_model):
    print(model.name)
    print(model.email)
    print(model.age)
    print(model.contact)
    print(model.allergies)
    print(model.married)
    print(model.linkedIn)
    print("updated to DB")
data={"name":"Isha","email":"itsishanegi@gmail.com","linkedIn":"https://linkedin.com","age":'20','weight':45.7,"contact":{"phone":"2868276"},"married":True} #valid with this str datatype -> '20' -->must be using .isdigit() function internally
# data={"name":"Isha","age":20} #valid with this too
# data={"name":"Isha","age":'twenty'} #invalid with english 'twenty'
obj=My_model(**data)
insert_data(obj)
# update_data(obj)
data2={"name":"nitish sir","email":"itsfgsegi@gmail.com","linkedIn":"https://linkedin.com","age":33,'weight':77.7,"contact":{"phone":"288723976"},"allergies":["dust"]}
obj1=My_model(**data2)
update_data(obj1)
