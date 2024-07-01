from src import Teacher, Student, student_validate, teacher_validate


if __name__ == "__main__":
    teacher = Teacher()
    student = Student()
    again = 'y'     
    while again == 'y':
        print("Press: ")
        print("1 for teacher data control")
        val1 = int(input("2 for student data control: "))
        match val1:
            case 1:
                print("Press:")
                print("1 for input")
                print("2 for display data")
                print("3 for search data")
                val2 = int(input("4 for delete data: "))
                match val2:                      
                    case 1:
                        teacher.input()
                        
                    case 2:
                        if teacher_validate():
                            teacher.display_data()
                        
                        
                    case 3:
                        if teacher_validate():
                            teacher.search_data()
                        
                    
                    case 4:
                        if teacher_validate():
                            teacher.delete_data()
                        
                    
                    case default:
                        print("Invalid for teacher data control!!!")
                        
            case 2:
                print("Press:")
                print("1 for input")
                print("2 for display data")
                print("3 for search data")
                val3 = int(input("4 for delete data: "))
                match val3:
                    case 1:
                        if teacher_validate():
                            student.input()
                    case 2:
                        if teacher_validate():
                            student.display_all_data()
                    case 3:
                        if teacher_validate():
                            student.search_data()
                        
                    
                    case 4:
                        if teacher_validate():
                            student.delete_data()
                        

                    case default:
                        print("Invalid for student data control!!!")
            case default:
                print("Invalid!!")
        again = input("Do you want to continue? (y/n): ").lower()
