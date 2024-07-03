import json
import os
def data_validation(data):
    """
    Validates the given data dictionary by checking if it contains all the required fields and if the student's roll, email, and phone number are unique.

    Parameters:
        data (dict): A dictionary containing the data to be validated. It should have the following keys: "name", "roll", "phone", "email", "address", and "marks".

    Returns:
        bool: True if the data is valid, False otherwise.

    Raises:
        None

    Examples:
        >>> data = {
        ...     "name": "John Doe",
        ...     "roll": "12345",
        ...     "phone": "1234567890",
        ...     "email": "john.doe@example.com",
        ...     "address": "123 Main St",
        ...     "marks": "85"
        ... }
        >>> data_validation(data)
        True

        >>> data = {
        ...     "name": "Jane Doe",
        ...     "roll": "12345",
        ...     "phone": "1234567890",
        ...     "email": "jane.doe@example.com",
        ...     "address": "456 Main St",
        ...     "marks": "90"
        ... }
        >>> data_validation(data)
        False
    """
    try:
        flag = 0
        if data["name"] and data["roll"] and data["phone"] and data["email"] and data["address"] and data["marks"]:
            filename = "files/studentrecord.json"
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    json_content = json.load(file)
                    for data_dict in json_content:
                        if data["roll"] == data_dict["roll"]:
                            flag = 1
                        elif data["email"] == data_dict["email"]:
                            flag = 1
                        elif data['phone'] == data_dict['phone']:
                            flag = 1
                    if flag == 1:
                        raise ValueError("Invalid data!!!")
                    else:
                        return True
            else:
                return True
            
                        
    except ValueError as v:
            print(v)
            return False