# Create an Employee class 

class Employee:
    def __init__(self,employee_name,employee_id,title,department):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.title = title
        self.department = department
    
    def display_employee_details(self):
        print(f'Employee name: {self.employee_name} Employee id: {self.employee_id} Employee title: {self.title} Employee department: {self.department}')

    def __str__(self):
        return f'{self.employee_name}, id: {self.employee_id}'

# The Employee class and it's methods and attributes are created as per instructions
# Now create the Department class
    
class Department:
    def __init__(self,department_name):
        self.department_name = department_name
        self.employees = []

    # you can add an employee to the employees list by using this function
    def add_employee(self,employee):
        self.employees.append(employee)

    # you can remove an employee from the employees list by checking whether the employee exists in the list or not using employee_id
    def remove_employee(self,employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                self.employees.remove(emp)
                return True
        return False

    # you can list all the employees present in the department using this function.
    def list_employees(self):
        if self.employees:
            for emp in self.employees:
                emp.display_employee_details()
        else:
            print('There are no employees in this department')


# The Department class is completed as per the specifications 
# Now let's create the Company class 
            
class Company:
    def __init__(self):
        self.departments = {}

    # you can add department by using the department_name attribute in Department class
    def add_department(self,department):
        self.departments[department.department_name] = department
    
    # you can remove the department by using the department_name variable whether it exists in the dictionary or not.
    def remove_department(self,department_name):
        if department_name in self.departments:
            del self.departments[department_name]
        else:
            print('This department does not exist')
    
    # you can list all the departments present and their corresponding employees also using this function
    def display_departments(self):
        if self.departments:
            for k,v in self.departments.items():
                print(f'Department: {k}')
                v.list_employees()
                print()
        else:
            print('There are no departments in this company')

    # you can save all the information to a text document using write function of python named compant_data
    def save_file(self,file_name):
        with open(file_name,'w') as f:
            for k,v in self.departments.items():
                f.write(f'Department: {k}\n')
                for emp in v.employees:
                    f.write(f'Name: {emp.name} id: {emp.id} title: {emp.title}')
            f.write('\n')


# It is an user guide for the users with clear instruction like what kind of functionality they want to perform
def user_guide():
    ''' welcome to the Employee Management System '''
    menu = """
    Choose below options for different functionalities:
    1. Press 1. to Add a department
    2. Press 2. to remove a department
    3. Press 3. to display all existing departments
    4. Press 4. to add an employee
    5. Press 5. to remove an employee
    6. Press 6. to save the file to text document
    7. Press 7. to exit
    """
    print(menu.strip())


# It is an main function where when the users choose the options from the above user guide to perform the CRUD operations.
def main():
    c = Company()
    file_name = 'company_data.txt'

    while True:
        user_guide()
        option = input('Enter your option:')

        # if the users chooses the first option to add department 
        # we store the input in the variable and add to the departments dictionary
        if option == '1':
            department_name = input('Enter the department name:')
            department = Department(department_name)
            c.add_department(department)

        #if chooses to remove the department then using the department name we can remove it
        elif option == '2':
            department_name = input('Enter department to be removed')
            if department_name in c.departments:
                c.remove_department(department_name)
            else:
                print('The department does not exist')
        
        # if you choose to dispaly all departments then from company class run the display departments method
        elif option == '3':
            c.display_departments()

        # if you want add an employee to the department first check whether the department exists or not.
        # Then fill the variable and pass them to employee class.
        elif option == '4':
            name = input('Enter the employee name:')
            id = input('Enter the employee id:')
            title = input('Enter the employee title:')
            department = input('Enter the employee department:')

            if department in c.departments:
                employee = Employee(name,id,title,department)
                c.departments[department].add_employee(employee)
            else:
                print('Department does not exist')
        
        # if you want to remove the employee 
        # loop through the departments values and match the employee id
        elif option == '5':
            emp_id = input('Enter the employee id to be removed:')
            for dept in c.departments.values():
                if dept.remove_employee(emp_id):
                    print('Employee removed successfully')
                    break
                else:
                    print('Employee does not exist')

        elif option == '6':
            try:
                c.save_file(file_name)
                print('Data saved to file')
            except Exception as e:
                print(f'Error saving data to file: {e}')
        
        elif option == '7':
            break

        else:
            print("Invalid choice. Please enter a valid option")


if __name__ == "__main__":
    main()







            


