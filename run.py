from db_products_oop import *
from db_employees_oop import *
products_table = NWProducts()
employees_table = NWEmployees()

while True:
    print("-----------------------------")
    print('Choose 1 to get all products')
    print('Choose 2 to get one product from the product ID')
    print('Choose 3 to get the ten cheapest products')
    print('Choose 4 to get the ten most expensive products')
    print('Choose 5 to search for a product by name')
    print('Choose 6 to get all employee data')
    print('Choose 7 to get an employee from their employee ID')
    print('Choose 8 to get an employee from their last name')
    print('Choose 9 to create an employee')
    print("-----------------------------")
    ui = input("Choose an appropriate number: ").strip()

    if ui == '1':
        print("Getting all products")
        products_table.print_all()

    elif ui == '2':
        print("Getting one product")
        id = int(input("What is the product ID?").strip())
        product = products_table.read_one(id)
        row = product.fetchone()
        print(f"ID: {row.ProductID} - {row.ProductName}  £{row.UnitPrice}")

    elif ui == '3':
        print("Getting the ten cheapest products")
        products_table.print_cheap_10()

    elif ui == '4':
        print("Getting the ten most expensive products")
        products_table.print_expensive_10()

    elif ui == '5':
        prod_name = input("What is the name of the product? ")
        products_table.search_by_name(prod_name)

    elif ui == '6':
        print("Getting all employee data")
        data = employees_table.emp_read_all()
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.EmployeeID} // {row.TitleOfCourtesy} {row.FirstName} {row.LastName} - {row.Title} // Address: {row.Address} {row.PostalCode}, {row.City} // Phone: {row.HomePhone} // DOB: {row.BirthDate}")

    elif ui == '7':
        id = int(input("What is the Employee ID?").strip())
        print("Getting the employee")
        employee = employees_table.emp_read_one(id)
        row = employee.fetchone()
        print(f"ID: {row.EmployeeID} // {row.TitleOfCourtesy} {row.FirstName} {row.LastName} - {row.Title} // Address: {row.Address} {row.PostalCode}, {row.City} // Phone: {row.HomePhone} // DOB: {row.BirthDate}")

    elif ui == '8':
        emp_name = input("What is the employee's last name? ")
        employees_table.search_emp_by_name(emp_name)

    # create an employee
    elif ui == '9':
        print('Creating an employee')
        first_name = input("What is the employee's first name ")
        last_name = input("What is the employee's last name ")
        employees_table.create_employee(first_name, last_name)

    elif "bye" in ui or "exit" in ui:
        print("Goodbye! Thank you")
        break

    else:
        print("I didn't quite catch that. Please choose an available option")