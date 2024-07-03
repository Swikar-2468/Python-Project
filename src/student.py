import json
import os
# from teacher import Teacher
from .teacher import Teacher
from .student_validate import data_validation

class Student:
    def __init__(self):
        pass

    def calculations(self, data):
        
        if data['marks']['maths'] >= 40 and data['marks']['physics'] >= 40 and data['marks']['chemistry'] >= 40:
            data['remarks'] = "pass"
            data['percentage'] = sum(data['marks'].values()) / len(data['marks'])
        else:
            data["remarks"] = "fail"
            data['percentage'] = "---"
        data['max_marks'] = max(data['marks'].values())
        data['min_marks'] = min(data['marks'].values())
        return data

    def input(self):
        """
        Takes input from the user for student details, validates the input data, and saves it to a JSON file.
        No parameters.
        No return value.
        """
        teacher = Teacher()
        studentlist = []
        filename = "files/studentrecord.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:    
                studentlist = json.load(file)

        studentdict = {}
        marks_dict = {}
        studentdict['name'] = input("Name: ").title()
        studentdict['roll'] = int(input("Class-roll: "))
        studentdict['address'] = input("Address: ").title()

        phone = int(input("Phone: "))
        while not teacher.validate_phone(phone):
            phone = input("Phone: ")
        studentdict['phone'] = phone

        email = input("Email: ")
        while not teacher.validate_email(email):
            email = input("Email: ")
        studentdict['email'] = email
        
        # making a dictionary including marks of students in maths, phyics and chemistry
        marks_dict['maths'] = int(input("Enter your marks in maths: "))
        marks_dict['physics'] = int(input("Enter your marks in physics: "))
        marks_dict['chemistry'] = int(input("Enter your marks in chemistry: "))
        studentdict['marks'] = marks_dict
        
        # checking if the data entered by the user is already present in the JSON file
        if data_validation(studentdict):
            studentdict = self.calculations(studentdict)
            studentlist.append(studentdict)
            with open(filename, "w") as file:    
                json.dump(studentlist, file)
        else:
            print("The data you entered is repeated. Please try again.")

    def display(self, data):
        print(f"The name of the student is: {data['name']}")
        print(f"The roll of the student is: {data['roll']}")
        print(f"The phone of the student is: {data['phone']}")
        print(f"The email of the student is: {data['email']}")
        print(f"The address of the student is: {data['address']}")
        print(f"The marks of the student is: {data['marks']}")
        print(f"The student is: {data['remarks']}")
        if data['remarks'] == "pass":
            print(f"The percentage of the student is: {data['percentage']}%")
        print(f"The max marks of the student is: {data['max_marks']}")
        print(f"The min marks of the student is: {data['min_marks']}")
        


    def display_all_data(self):
        """
        Displays all the data of students stored in a JSON file.

        This function reads the student record JSON file, iterates over each student's data, and prints their 
        name, roll, phone, email, address, marks in maths, physics, and chemistry, and remarks. 
        If the JSON file does not exist, it prints "No data to display!!"

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        filename = "files/studentrecord.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                json_content = json.load(file)
                for data in json_content:
                    self.display(data)

        else:
            print("No data to display!!")
            
    
    def search_data(self):
        filename = "files/studentrecord.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                json_content = json.load(file)
                check_roll = int(input("Roll of person you want to have information of: "))
                
                for data in json_content:
                    if check_roll == data['roll']:    
                        self.display(data)
                        return
                print(f"Invalid roll: {check_roll}")
                return                    
        else:
            print("No data found.")


    def delete_data(self):
        """
        Deletes data from the teacher record file.

        This function prompts the user to enter the name of the person whose information they want to delete. It then checks if the file "stduentrecord.json" exists. If it does, it reads the contents of the file and loads it into a JSON object. It then iterates over each data entry in the JSON object and checks if the entered name matches the name in the data entry. If a match is found, the data entry is removed from the JSON object. The function returns after the first match is found. If the file does not exist, it prints "No data found."

        Parameters:
            None
        
        Returns:
            None
        """
        filename = "files/studentrecord.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                json_content = json.load(file)
                check_roll = int(input("Roll of student you want to delete the information of: "))
                
                for data in json_content:
                    if check_roll == data['roll']:
                        json_content.remove(data)
                        break
            with open(filename, "w") as file:
                json.dump(json_content, file)
        else:
            print("No data found.")

