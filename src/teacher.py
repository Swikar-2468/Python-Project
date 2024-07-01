import json
import os

class Teacher:
    def __init__(self):
        pass

    def validate_email(self, email):
        """
        Validates the format of an email address.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.

        Raises:
            ValueError: If the email address is invalid.
        """
        
        try:
            flag = 0
            local_name, domain = email.split('@')
            if not local_name or not domain:
                flag = 1
            if '..' in email:
                flag = 1
            if domain.startswith('.') or domain.endswith('.'):
                flag = 1
            if local_name.startswith('.') or local_name.endswith('.'):
                flag = 1
            if '.' not in domain:
                flag = 1
            if flag == 1:
                raise ValueError("Invalid email address. Please try again.")
            else:
                return True
                   
        except ValueError as v:
            print(v)
            return False
    
    
    def validate_phone(self, phone):
        """
        A function to validate a phone number.

        Parameters:
            phone (int): The phone number to validate.

        Returns:
            bool: True if the phone number is valid (10 digits), False otherwise.

        Raises:
            ValueError: If the phone number is invalid and should be tried again.

        """
        
        try:    
            if len(str(phone)) == 10:
                return True
            else:
                raise ValueError("Invalid phone number. Please try again.")
            
        except ValueError as v:
            print(v)
            return False

    def input(self):
        """
        Prompts the user to input teacher information and validates it before storing it in a JSON file.

        This function reads the existing teacher records from the 'teacherrecord.json' file, if it exists.
        It then prompts the user to input the teacher's name, ID, subject, address, phone number, and email.
        The phone number and email are validated using the 'validate_phone' and 'validate_email' methods, respectively.
        If the input is invalid, the user is prompted to try again.
        The input is stored in a dictionary and appended to the 'teacherlist' list.
        Finally, the updated 'teacherlist' is written back to the 'teacherrecord.json' file.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        teacherlist = []
        filename = "files/teacherrecord.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:    
                teacherlist = json.load(file)

        teacherdict = {}
        teacherdict['name'] = input("Name: ").title()
        teacherdict['id'] = input("ID: ")
        teacherdict['subject'] = input("Subject: ").title()
        teacherdict['address'] = input("Address: ").title()
        phone = int(input("Phone: "))
        while not self.validate_phone(phone):
            phone = input("Phone: ")
        teacherdict['phone'] = phone
        
        email = input("Email: ")
        while not self.validate_email(email):
            print("Invalid email. Please try again.")
            email = input("Email: ")
        teacherdict['email'] = email

        teacherlist.append(teacherdict)
        with open(filename, "w") as file:    
            json.dump(teacherlist, file)
                                  

    def display_data(self):
        """
        Displays the information of all teachers stored in the "teacherrecord.json" file.

        This function reads the "teacherrecord.json" file and prints the name, subject, email, and phone number of each teacher.

        Parameters:
            None

        Returns:
            None
        """
        filename = "files/teacherrecord.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                json_content = json.load(file)
                for data in json_content:
                    print(f"Name of the teacher is: {data['name']}")
                    print(f"Subject of the teacher is: {data['subject']}")
                    print(f"Email of the teacher is: {data['email']}")
                    print(f"Phone number of the teacher is: {data['phone']}")
                    
        else:
            print("No data found.")

    def search_data(self):
        """
        This function searches for a person's information in the "teacherrecord.json" file based on the input name.
        
        Parameters:
            None
        
        Returns:
            None
        """
        filename = "files/teacherrecord.json"
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

        This function prompts the user to enter the name of the person whose information they want to delete. It then checks if the file "teacherrecord.json" exists. If it does, it reads the contents of the file and loads it into a JSON object. It then iterates over each data entry in the JSON object and checks if the entered name matches the name in the data entry. If a match is found, the data entry is removed from the JSON object. The function returns after the first match is found. If the file does not exist, it prints "No data found."

        Parameters:
            None
        
        Returns:
            None
        """
        filename = "files/teacherrecord.json"
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
