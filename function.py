# Built-in Functions

marks = [75, 80, 65, 90, 85]

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Number of Subjects:", len(marks))


# 1. Required Positional Argument

def student(name):
    print("Student Name:", name)

student("siddhi")


print("\n-----------------------------")


# 2. Default Argument

def city(name, city="Junagadh"):
    print(name, city)

city("siddhi")
city("shree", "Rajkot")


print("\n-----------------------------")


# 3. Arbitrary Arguments (*args)

def subjects(*sub):
    print(sub)

subjects("Python")
subjects("Python", "Java")
subjects("Python", "Java", "HTML", "CSS")


print("\n-----------------------------")


# 4. Keyword Arguments (**kwargs)

def student_info(**info):
    print(info)

student_info(name="siddhi", age=19)
student_info(name="shree", age=22, course="Python")


print("\n-----------------------------")


# 5. __doc__ Attribute

def multiplication(*numbers):
    """This function returns multiplication of given numbers."""
    
    result = 1
    
    for n in numbers:
        result = result * n
    
    print("Multiplication:", result)


multiplication(2, 3)
multiplication(2, 3, 4)

print("\nDocumentation:")
print(multiplication.__doc__)