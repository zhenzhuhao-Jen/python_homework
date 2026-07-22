# Task 3

import csv

with open('../csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    my_list = list(reader)
    
    employee_name = [row[1] + ' ' + row[2]
                     for row in my_list  if row != my_list[0]]
    
    print(employee_name)

    e_name_list = [i for i in employee_name  if "e" in i]

    print(e_name_list)