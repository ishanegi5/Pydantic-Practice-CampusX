from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin:str
class Patient(BaseModel):
    name:str
    age:int=5
    address:Address
address_data={"city":"Dehradun","state":"uttarakhand","pin":"324"}

address_obj=Address(**address_data)
data={"name":"Isha","address":address_obj}
patient_obj=Patient(**data)
print(address_obj.city)
print(patient_obj.name)
print(patient_obj.address.state) 
print(patient_obj)
temp=patient_obj.model_dump()
print(temp)
print(type(temp))

temp_json=patient_obj.model_dump_json()
print(temp_json)
print(type(temp_json))

temp_json=patient_obj.model_dump_json(exclude_unset=True)
print(temp_json)
print(type(temp_json))