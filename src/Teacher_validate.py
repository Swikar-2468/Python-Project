import json
import os
class AuthenticationError(Exception):
    """
    Exception raised when there is an authentication error.
    """
    def __init__(self, message):
        super().__init__(message)


def authenticate_teacher(name, id):
    """
    Authenticate a teacher based on their name and ID.

    Args:
        name (str): The name of the teacher.
        id (int): The ID of the teacher.

    Returns:
        bool: True if the teacher is authenticated, False otherwise.

    Raises:
        None

    This function reads the teacher data from the "data_files/Teacher.json" file and checks if the provided name and ID match any of the teachers in the file. If a match is found, the function returns True. Otherwise, it returns False.
    """

    with open("files/teacherrecord.json") as file:
        teacher_data = json.load(file)
        for teacher in teacher_data:
            for data in teacher_data:
                if  name == data['name'] and id == data['id']:
                    print("Teacher authenticated.")
                    return True        
        return False


def teacher_validate():
    """
    A function that adds new data after authenticating the teacher.
    
    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    try:
        print("You need to validate your name and id.")
        name = input("Enter your name: ").title()
        id = input("Enter your ID number: ")
    
        if authenticate_teacher(name, id):
            print("Authentication successful. You may proceed.")
            return True
        else:
            raise AuthenticationError("Authentication failed. Invalid name or ID.")
    except AuthenticationError as e:
        print(e)
        return False
    
if __name__ == "__main__":
    teacher_validate()