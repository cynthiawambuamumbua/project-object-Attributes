# Submit a document describing your group's project in one paragraph
#  and a list of all objects that will form the project's implementation.
# For each object, write a description of the object and list all its attributes
#  and what each of the attributes represents. 

# E.G
# If Student was an object in the project, it would have attributes such as
# First Name
# Last Name
# Date of Birth
# Email
# Phone Number
# Registration Number
class Student:
    def __init__(self, first_name, last_name,date_of_birth,age, gender, email, phone_number,registration_number,ID_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth=date_of_birth
        self.age = age
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.registration_number=registration_number
        self.ID_number=ID_number
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_date_of_birth(self):
        return f"You were born in {self.date_of_birth}"
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_registration_number(self):
        return f"Your registration number is {self.registration_number}"
    
    def get_ID_number(self):
        return f"Your Id number is {self.ID_number}"
    
student1 = Student("cynthia", "mumbua","16.3.2004", 19, "female", "cynthiamumbuawambua@gmail.com", "0713504579","058","1234568798")
print(student1.first_name)
print(student1.get_full_name())
print(student1.get_phone_number())
print(student1.get_date_of_birth())
print(student1.get_registration_number())
print(student1.get_ID_number())

