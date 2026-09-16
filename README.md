# 🎓 Student Management System

**Author:** Siddhi Gadhiya  
**Project Type:** Python Console Application  
**Language:** Python  

A simple console-based **Student Management System** designed to manage student records through an interactive menu. The program allows the user to add, display, search, update, and delete student information, as well as view the subjects offered.

---

## 📌 Program 1 — If-Else Student Management System

## 🎯 Project Objectives

- 📝 Add and store student information.
- 👥 Display all registered students.
- 🔍 Search for a particular student by name.
- ✏️ Update existing student information.
- 🗑️ Delete a student record.
- 📚 Display the subjects offered by the system.
- 🚪 Provide a simple exit option.
- 💻 Practice Python concepts using a menu-driven console application.

---

## ✨ Features & Functionality

### 1. 📝 Add Student

The program allows the user to enter the following details:

- Student Name
- Student Age
- Student Course

After entering the information, the student record is stored successfully.

**Example:**

```text
Enter your choice (1-7): 1
Enter student name:siddhi
Enter student age:19
Enter student course:ai
Student added successfully!!!
```

---

### 2. 👥 Display All Students

This option displays all the students currently stored in the system.

**Example:**

```text
-----------------Student List-------------------
{'name': 'siddhi', 'age': 19, 'course': 'ai'}
{'name': 'shree', 'age': 20, 'course': 'ml'}
```

---

### 3. 🔍 Search Student

The user can search for a student by entering their name.

If the student exists, their details are displayed.

If the student does not exist, the program displays:

```text
student not found??
```

---

### 4. ✏️ Update Student

The update option allows the user to modify an existing student's:

- Name
- Age
- Course

After successful modification, the program displays:

```text
Student updated successfully!!!
```

---

### 5. 🗑️ Delete Student

The delete option allows the user to remove a student record by entering the student's name.

After deletion, the program displays:

```text
Student deleted successfully!!!
```

---

### 6. 📚 Display Subjects Offered

The program displays the subjects available in the system:

```text
--------Subject Name--------
Python
C++
PHP
```

---

### 7. 🚪 Exit

The user can select option 7 to close the program.

```text
Thank you for using the student management system!
```

---

---

## 🧠 Python Concepts Used

- Variables
- Lists
- Dictionaries
- `while` loop
- `if`, `elif`, and `else`
- `for` loop
- User input using `input()`
- Integer conversion using `int()`
- Dictionary access
- List `append()`
- List `remove()`
- `break` statement
- Menu-driven programming

---

## 🗂️ Data Structure

Student information is stored using a **list of dictionaries**.

Each student record contains:

```text
name
age
course
```

For example:

```text
{'name': 'siddhi', 'age': 19, 'course': 'ai'}
```

Multiple student records can be stored in the same list.

---

## 🛠️ Technologies Used

- **Python 3.14.6**
- **Visual Studio Code**
- **Command Line / Terminal**

---

## 📌 Project Summary

The Student Management System is a beginner-friendly Python project that demonstrates how basic Python data structures and control statements can be combined to create a useful console application.

The interactive menu keeps running until the user selects the **Exit** option, making it possible to perform multiple student management operations in a single program run.

## 🚀 Future Improvements

The project can be extended in the future by adding:

- Student ID
- Date of Birth
- Email and phone number
- Multiple courses
- Marks and grades
- File/database storage
- Login system
- Graphical User Interface (GUI)

## 🖥️ Example Console Output

```text
-----------------student management system-------------------
Select an option:
1.Add student:
2.Display all student:
3.Search student
4.Update student
5.Delete student
6.Display subject offered
7.Exit:
Enter your choice (1-7): 1
Enter student name:siddhi
Enter student age:19
Enter student course:ai
Student added successfully!!!

-----------------student management system-------------------
Select an option:
1.Add student:
2.Display all student:
3.Search student
4.Update student
5.Delete student
6.Display subject offered
7.Exit:
Enter your choice (1-7): 1
Enter student name:shree
Enter student age:20
Enter student course:ml
Student added successfully!!!

-----------------student management system-------------------
Select an option:
1.Add student:
2.Display all student:
3.Search student
4.Update student
5.Delete student
6.Display subject offered
7.Exit:
Enter your choice (1-7): 2

-----------------Student List-------------------
{'name': 'siddhi', 'age': 19, 'course': 'ai'}
{'name': 'shree', 'age': 20, 'course': 'ml'}
```

---




## 📌 Program 2 — Match-Case Student Management System

---

## 🔹 What This Program Can Do

| Option | Operation            |
| ------ | -------------------- |
| 1      | Add Student          |
| 2      | Display Students     |
| 3      | Update Student       |
| 4      | Delete Student       |
| 5      | Search by Student ID |
| 6      | View Subjects        |
| 7      | Exit                 |

---

## 👨‍🎓 Student Record

For every student, the program stores four important details:

```text
Student ID
Student Name
Student Age
Student Course
```

The records are stored inside a **list containing dictionaries**.

Example:

```text
{'id': 1, 'name': 'Hari', 'age': 20, 'course': 'BCA'}
```

---

## ⚙️ Working of the Application

### ➕ Add Student

The user enters the student's ID, name, age, and course. The information is converted into a dictionary and added to the student list.

```text
Enter your id: 1
Enter your name: Hari
Enter your age: 20
Enter your course: BCA
Student Added!
```

### 📋 View Student Records

All currently stored student dictionaries are displayed on the screen.

```text
{'id': 1, 'name': 'Hari', 'age': 20, 'course': 'BCA'}
{'id': 2, 'name': 'Madhav', 'age': 21, 'course': 'BCA'}
```

### 🔄 Update Information

The user can enter a student ID and provide new information for the student record.

### ❌ Remove Student

A student can be deleted by entering the student's name.

```text
Enter name to delete: Madhav
student deleted
```

### 🔎 Find Student

The search option finds a student using their unique student ID.

```text
Enter id to search: 1

{'id': 1, 'name': 'Hari', 'age': 20, 'course': 'BCA'}
```

### 📚 Subjects

The application currently displays these subjects:

```text
----Display Subjects----
1.AI
2.Python
3.ML
```

---

## 🧩 Python Topics Practiced

This project provides practice with:

* Lists
* Dictionaries
* `while` loop
* `for` loop
* `match-case`
* `case`
* Conditional statements
* `input()` function
* Type conversion using `int()`
* `append()`
* `remove()`
* `break`
* Menu-driven programming

---

## 💻 Software Requirements

* Python 3.14.6
* Visual Studio Code
* Windows Command Prompt / Terminal

---

## ▶️ Running the Program

Save the Python file and run it using:

```text
python filename.py
```

After running the program, select any option from **1 to 7** and follow the instructions displayed on the screen.

---

## 📊 Sample Run

```text
1.add students
2.display all students
3.update student information
4.delete student
5.student id of search
6.display subjects offered
7.exit

enter your choice: 1

Enter your id: 1
Enter your name: Hari
Enter your age: 20
Enter your course: BCA
Student Added!

enter your choice: 1

Enter your id: 2
Enter your name: Madhav
Enter your age: 21
Enter your course: BCA
Student Added!

enter your choice: 2

{'id': 1, 'name': 'Hari', 'age': 20, 'course': 'BCA'}
{'id': 2, 'name': 'Madhav', 'age': 21, 'course': 'BCA'}
```

---

## 🌱 Possible Enhancements

Some features that can be added later are:

* Store data permanently in a file
* Connect the application with a database
* Add student marks
* Calculate grades
* Add email and contact details
* Create a graphical interface
* Add student login functionality

---

## 📌 Conclusion

The **Student Management System** is a simple and beginner-friendly Python console application developed to manage student records efficiently.

This project helped in understanding and applying important Python concepts such as **lists, dictionaries, loops, user input, and match-case statements**. It also demonstrates how a menu-driven program can be used to perform different operations on student data.

---

## 🖥️ Output

The following output shows the working of the Student Management System with sample student records:

```text
1.add students
2.display all students
3.update student information
4.delete student
5.student id of search
6.display subjects offered
7.exit

enter your choice: 1
Enter your id: 1
Enter your name: Hari
Enter your age: 20
Enter your course: BCA
Student Added!

enter your choice: 1
Enter your id: 2
Enter your name: Madhav
Enter your age: 21
Enter your course: BCA
Student Added!

enter your choice: 2

{'id': 1, 'name': 'Hari', 'age': 20, 'course': 'BCA'}
{'id': 2, 'name': 'Madhav', 'age': 21, 'course': 'BCA'}

enter your choice: 5
Enter id to search: 1

{'id': 1, 'name': 'Hari', 'age': 20, 'course': 'BCA'}

enter your choice: 6

----Display Subjects----
1.AI
2.Python
3.ML

enter your choice: 7
Thank you..
```