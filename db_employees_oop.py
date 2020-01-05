from db_connect_oop import *
 # employees_table = NWEmployees()

class NWEmployees(MSDBConnection):

    def __sql_query(self, sql_query): # Makes it private
        return self.cursor.execute(sql_query)

# Get all employee data
    def emp_read_all(self):
        query = "SELECT * FROM Employees"
        data = self.__sql_query(query)
        return data

# Get one employee by id
    def emp_read_one(self, id):
        query = f"SELECT * FROM Employees WHERE EmployeeID = {id}"
        data = self.__sql_query(query)
        return data

# Search for one employee by name or LastName
    def search_emp_by_name(self, last_name):
        query = f"SELECT * FROM Employees WHERE LastName LIKE '%{last_name}%'"
        data = self.__sql_query(query)
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.EmployeeID} // {row.TitleOfCourtesy} {row.FirstName} {row.LastName} - {row.Title} // Address: {row.Address} {row.PostalCode}, {row.City} // Phone: {row.HomePhone} // DOB: {row.BirthDate}")

     # create an employee
    def create_employee(self, first_name, last_name):
        query = f"INSERT INTO Employees (FirstName, LastName) VALUES ('{first_name}', '{last_name}')"
        data_to_insert = self.__sql_query(query)
        self.docker_Northwind.commit()
        return data_to_insert


# Add all this funtionality to our run products while loop

# employee = NWEmployees().emp_read_one(4)
# print(employee.fetchone())

# employee = NWEmployees().search_emp_by_name('Fuller')
