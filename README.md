# Pydantic Practice – CampusX

This repository contains my complete hands-on practice code for **Pydantic**, based on the CampusX tutorial.  
All examples were implemented manually in VS Code as I learned how Pydantic handles data validation, serialization, parsing, and model logic.

---

## 🚀 What I Practiced

This repo includes practice files covering:

### ✔ Core Pydantic Concepts
- Creating `BaseModel` classes
- Field definition & type enforcement
- Automatic parsing and validation

### ✔ Field Validators (`@field_validator`)
- Pre-validation (`mode="before"`)
- Post-validation (`mode="after"`)
- Custom validation logic for:
  - Email domains  
  - Name formatting  
  - Type conversions  
  - Value restrictions  

### ✔ Model Validators (`@model_validator`)
- Cross-field validation  
- Conditional business rules  
- Age-based rules + contact requirements  

### ✔ Nested Models
- Passing models inside models  
- Dict-to-model automatic conversion  
- Practical patient–address example  

### ✔ Computed Fields (`@computed_field`)
- Deriving values dynamically  
- BMI calculation example  

### ✔ Optional Fields & Defaults
- Proper use of `Optional`
- Required vs optional field behavior

---

## 🛠 Tech Used
- **Pydantic v2**
- **Python 3.x**
- **VS Code**

---

## 📁 Folder Purpose

This repository serves as:
- My personal practice reference  
- A collection of working Pydantic examples  
- A foundation for understanding **FastAPI**, which is built on top of Pydantic  
- A place to track my backend + data validation learning journey  

---

## ▶️ How to Run Any File

Make sure Python is installed:
Run an example:

python filename.py

🙏 Acknowledgment

Thanks to CampusX for their clean, beginner-friendly Pydantic explanation.
📌 Next Steps

I will soon move from Pydantic practice to:

Building APIs with FastAPI

Implementing request/response models

Real backend projects

Stay tuned for updates!
```bash
python --version
