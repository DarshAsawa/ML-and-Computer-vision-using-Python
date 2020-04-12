from prettytable import PrettyTable

x = PrettyTable()

#A table can be created with add_row() and add_column() methods.

#creating table using add_row() method.
x.field_names = ['States','Capital']

x.add_row(['Haryana','Chandigarh'])
x.add_row(['Andhra Pradesh','Hyderabad'])
x.add_row(['Goa','Panaji'])

print(x)

#creating table using add_column method.

y = PrettyTable()
column_names = ["Country","Captical"]

y.add_column(column_names[0],["India","China","Japan"])
y.add_column(column_names[1],["New Delhi","Beijing","Tokyo"])

print(y)

