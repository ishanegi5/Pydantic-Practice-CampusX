from pydantic import BaseModel,EmailStr,field_validator,model_validator,computed_field
from typing import Dict,Optional
class My_class(BaseModel):
    name: str
    email: EmailStr
    contact: Optional[Dict[str,int]]=None
    age: int
    height:float
    weight: float
    @field_validator("email",mode="before")
    def check_f(cls,value):
        offer_for=["hdfc.com","icici.com"]
        domain_name=value.split("@")[-1]
        if(domain_name in offer_for):
            return value
        raise ValueError("wrong domain")
    @field_validator('name',mode='before')
    def name_check(cls,value):
        if(value[0]==value[0].upper()):
            return value
        raise ValueError('first letter is not capital in name')
    @model_validator(mode="after")
    def validate_age_emergency(self):
        if(self.age>60 and (not(self.contact) or "emergency" not in self.contact)):
            raise ValueError("Patients more than 60 should have emergency contact")
        return self
    @computed_field
    @property
    def bmi(self)-> float:
        return round(self.weight/(self.height)**2,2)
def insert_f(model:My_class):
    print(model.name)
    print(model.email)
    print(model.age)
    print(model.contact)
    print(model.bmi)
data1={"name":"Isha negi","email":"isha@icici.com","age":79,"contact":{'emergency':2548955},"height":2.7,"weight":4.8}
obj1=My_class(**data1)
insert_f(obj1)