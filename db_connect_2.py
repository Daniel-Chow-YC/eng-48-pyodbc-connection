import pyodbc

# These are our variables to connect
server = 'localhost,1433'
database = 'airport'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
docker_airport = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Making a cursor
cursor = docker_airport.cursor()

# Executing sql commands
cursor.execute("SELECT * FROM Passengers;")

# Cursor will maintain states
# Fetching data from the executed SQL command and printing
row = cursor.fetchone()
print(row)
