import pyodbc
from db_connect_oop import *

class NWProducts(MSDBConnection):

    def __sql_query(self, sql_query): # Makes it private
        return self.cursor.execute(sql_query)

    def read_all(self):
        # build our sql query
        query = "SELECT * FROM Products"
        # execute our query
        data = self.__sql_query(query)
        # return an iterable object
        return data

    # Read one - using ID
    def read_one(self, id):
        query = f"SELECT * FROM Products WHERE ProductID = {id}"
        data = self.__sql_query(query)
        return data

    # Prints all products using the while loop and fetchone
    def print_all(self):
        query = "SELECT * FROM Products"
        data = self.__sql_query(query)
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.ProductID} - {row.ProductName}  £{row.UnitPrice}")

    # prints top 10 products by price - formatted (cheapest)
    def print_cheap_10(self):
        query = "SELECT TOP 10 * FROM Products ORDER BY UnitPrice"
        data = self.__sql_query(query)
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.ProductID} - {row.ProductName}  £{row.UnitPrice}")

    # prints bottom 10 products by price - formatted
    def print_expensive_10(self):
        query = "SELECT TOP 10 * FROM Products ORDER BY UnitPrice DESC"
        data = self.__sql_query(query)
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.ProductID} - {row.ProductName}  £{row.UnitPrice}")

    # Search product by name
    def search_by_name(self, prod_name):
        query = f"SELECT * FROM Products WHERE ProductName LIKE '%{prod_name}%'"
        data = self.__sql_query(query)
        while True:
            row = data.fetchone()
            if row is None:
                break
            print(f"ID: {row.ProductID} - {row.ProductName}  £{row.UnitPrice}")



# product = NWProducts().search_by_name('Konbu')


# exp = NWProducts().print_cheap_10()
# all_products = NWProducts().print_all()



# products = NWProducts().read_all()
#
# print(products.fetchone())

# products = NWProducts().read_one(7)
# print(products.fetchone())







    # Read / list all

    # read one

    # ask for input --> front end -- input()
    # create one --> makes things persistent in DB

    # update one

    # destroy one