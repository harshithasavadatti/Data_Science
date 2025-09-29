# 📂 IT Tickets JSON Loader 
A hands-on practice project to explore **Python**, **Pandas**, **JSON handling**, and **exception handling** all in one place.

---

## ✨ Overview  
This notebook demonstrates how to:
- Load multiple JSON files containing IT ticket data  
- Flatten nested JSON fields like `user.name`, `user.department`, `user.email`  
- Handle exceptions gracefully when files or fields are missing  
- Create new computed columns for additional insights  

---

## 📝 Features  
- **Flexible JSON Loading**: Works with multiple JSON files at once  
- **Flatten Nested Data**: Automatically extracts nested user details  
- **Custom Insight Columns**:
  - `name_length` → length of the user’s name  
  - `department_length` → length of the department name  
  - `email_length` → length of the user’s email  
- **Robust Exception Handling**: Skips problematic files without crashing  

---

## 🛠 Tech Stack  
- Python 3.13  
- Jupyter Notebook  
- Pandas  

