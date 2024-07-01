import json
import os
# from teacher import Teacher
from .teacher import Teacher
from .student_validate import data_validation

class Student:
    def __init__(self):
        pass

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
        marks_list = []
        print("Enter your details")
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
        
        print("Enter your marks in maths, physics, chemistry: ")
        for _ in range(3):
            marks_list.append(int(input()))

        studentdict['marks'] = marks_list
        studentlist.append(studentdict)
        
        if data_validation(studentdict):
            with open(filename, "w") as file:    
                json.dump(studentlist, file)
        else:
            print("Invalid data")

    def calculations(self):
        """
        Calculates the remarks for each student based on their marks and updates the student record JSON file.

        This function reads the student record JSON file, iterates over each student's data, and checks if all of their marks are greater than or equal to 40. If so, the student's remark is set to "pass", otherwise it is set to "fail". The updated student record JSON file is then written back to the file.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        with open("files/studentrecord.json", "r") as file:    
            json_content = json.load(file)
            for data in json_content:
                if all(mark >= 40 for mark in data['marks']):
                    data["remarks"] = "pass"
                else:
                    data["remarks"] = "fail"
                data['max_marks'] = max(data['marks'])
                data['min_marks'] = min(data['marks'])
                # to calculate the percentage of these marks for each student
                if data['min_marks'] > 40:
                    data['percentage'] = sum(data['marks']) / len(data['marks'])

            
            with open("files/studentrecord.json", "w") as file:
                json.dump(json_content, file)

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
        self.calculations()
        if os.path.exists(filename):
            with open(filename, "r") as file:
                json_content = json.load(file)
                for data in json_content:
                    print(f"The name of the student is: {data['name']}")
                    print(f"The roll of the student is: {data['roll']}")
                    print(f"The phone of the student is: {data['phone']}")
                    print(f"The email of the student is: {data['email']}")
                    print(f"The address of the student is: {data['address']}")
                    print(f"The marks of the student in maths, physics and chemistry are {data['marks']}")
                    print(f"The student is: {data['remarks']}")
                    print(f"The max marks of the student is: {data['max_marks']}")
                    print(f"The min marks of the student is: {data['min_marks']}")
                    if data['remarks'] == "pass":
                        print(f"The percentage of the student is: {data['percentage']}%")

        else:
            print("No data to display!!")
            
    
    def search_data(self):
        filename = "files/studentrecord.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                json_content = json.load(file)
                check_name = input("Name of person you want to have information of: ").title()
                
                for data in json_content:
                    if check_name in data['name']:    
                        print(data)
                        return
                print(f"Invalid name: {check_name}")
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
                check_name = input("Name of person you want to delete the information of: ").title()
                
                for data in json_content:
                    if check_name in data['name']:
                        json_content.remove(data)
                        return                    
                    
        else:
            print("No data found.")

