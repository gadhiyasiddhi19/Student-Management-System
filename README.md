# 🎓 STUDENT MANAGEMENT SYSTEM 
 
A Python-Based Console Application for Managing Student Records 
 
**Author:** Siddhi Gadhiya   
**Python Version:** 3.14.6   
**Environment:** Visual Studio Code 
 
--- 
 
## 📌 PROJECT DESCRIPTION 
 
**Student Management System** is a Python-based console application designed to manage student records using different Python collection data types. 
 
The program allows users to add, display, search, update, and delete student information. It also provides an option to display all unique subjects offered by the students. 
 
This project is created as a Python Practical Assignment to understand and implement **List, Dictionary, Tuple, and Set** collections. 
 
--- 
 
## 🎯 PROJECT OBJECTIVES 
 
- Manage student information using Python. 
- Understand and practice Python collection data types. 
- Use Lists to store multiple student records. 
- Use Dictionaries to store student information. 
- Use Tuples to store Student ID and Date of Birth. 
- Use Sets to store unique subjects. 
- Implement CRUD operations. 
- Understand loops and conditional statements. 
- Handle user input and type conversion. 
- Display student records in the console. 
 
--- 
 
## ✨ FEATURES 
 
### 👤 1. Add Student 
 
- Add a new student record. 
- Take Student ID, Name, Age, Grade, Date of Birth, and Subjects as input. 
- Store Student ID and Date of Birth in a Tuple. 
- Store subjects using a Set. 
- Store complete student information in a Dictionary. 
- Add the student record to the Students List. 
 
**Student Information:** 
 
- Student ID 
- Name 
- Age 
- Grade 
- Date of Birth 
- Subjects 
 
### 📋 2. Display All Students 
 
- Display all stored student records. 
- Show Student ID, Name, Age, Grade, Date of Birth, and Subjects. 
- Use a `for` loop to display each student. 
 
### 🔍 3. Search Student 
 
- Search for a student using Student ID. 
- Display student details if the ID is found. 
- Display a "Student not found" message if the ID does not exist. 
 
### ✏️ 4. Update Student 
 
- Search for a student using Student ID. 
- Update student name. 
- Update student age. 
- Update student grade. 
- Display a success message after updating. 
 
### 🗑️ 5. Delete Student 
 
- Search for a student using Student ID. 
- Delete the selected student record. 
- Display a success message after deletion. 
 
### 📚 6. Display Subjects Offered 
 
- Display all unique subjects from student records. 
- Use Set operations to combine subjects. 
- Avoid duplicate subjects. 
 
### 🚪 7. Exit 
 
- Exit the program using the `break` statement. 
- Display a thank-you message before exiting. 
 
--- 
 
## 🛠 TECHNOLOGIES USED 
 
| Technology | Details | 
|------------|---------| 
| Python | 3.14.6 | 
| IDE | Visual Studio Code | 
| Interface | Console / Terminal | 
| Version Control | Git & GitHub | 
 
--- 
 
## 📚 PYTHON CONCEPTS COVERED 
 
- Lists (`list`) 
- Dictionaries (`dict`) 
- Tuples (`tuple`) 
- Sets (`set`) 
- `while` loop 
- `for` loop 
- `if-elif-else` 
- User Input (`input()`) 
- Type Conversion (`int()`) 
- `append()` 
- `del` 
- `break` 
- `split()` 
- `join()` 
- Set Union Operations 
- Dictionary Access 
- List Manipulation 
 
--- 
 
## 📂 PROJECT STRUCTURE 
 
```text
Collection-Manipulator/
│
├── stud_manage_system_if_else.py
└── README.md


🖥️ SAMPLE OUTPUT

-----------------student management system-------------------
Select an option:
1. Add student
2. Display all student
3. Search student
4. Update student
5. Delete student
6. Display subject offered
7. Exit

Enter your choice (1-7): 1
Enter student id: 101
Enter student name: siddhi
Enter student age: 19
Enter student grade: 90
Enter student date of birth (yyyy-mm-dd): 2007-04-15
Enter student subjects (comma-separated): python
Student added successfully!!!

-----------------student management system-------------------
Select an option:
1. Add student
2. Display all student
3. Search student
4. Update student
5. Delete student
6. Display subject offered
7. Exit

Enter your choice (1-7): 2

--- Display All Students ---
Student ID: 101 | Name: siddhi | Age: 19 | Grade: 90 | Date of Birth: 2007-04-15 | Subjects: python

-----------------student management system-------------------
Select an option:
1. Add student
2. Display all student
3. Search student
4. Update student
5. Delete student
6. Display subject offered
7. Exit

Enter your choice (1-7): 7
Thank you for using the student management system!