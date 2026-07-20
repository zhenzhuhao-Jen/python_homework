# Task 2
import traceback
import csv
def read_employees():
    empty_dict = dict()
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            empty_dict["fields"] = next(reader)

            for row in reader:
                rows.append(row)

            empty_dict["rows"] = rows
        return empty_dict   
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
employees = read_employees()
#print(employees)

# Task 3
def column_index(x):
    
    return employees["fields"].index(x)

employee_id_column = column_index("employee_id")


# Task 4

#print(first_name_index)

def first_name(rowNum):
    first_name_index = column_index("first_name")
    return employees["rows"][rowNum][first_name_index]


# Task 5
def employee_find(integer):
    employee_id = integer 
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))

    return matches

# Task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7
last_name_column = column_index("last_name")
def sort_by_last_name():
    
    last_name = lambda row: row[last_name_column]
    employees["rows"].sort(key=last_name)
    
    return(employees["rows"])
sort_by_last_name()
#print(employees)

# Task 8
#print(employees["fields"])
#print(employees["rows"][3])
def employee_dict(row):
    row_dict = {}
    keys = employees["fields"][1:]
    values = row[1:]
    row_dict = dict(zip(keys, values))
    return row_dict
#print(employee_dict(employees["rows"][3]))

#Task 9
def all_employees_dict(): 
    all_dict = {}
    for row in employees["rows"]:
        all_dict[row[0]] = employee_dict(row)
    return all_dict
#print(all_employees_dict())

#Task 10
import os
def get_this_value():
    bariable = os.getenv("THISVALUE")
    return bariable
print(get_this_value())

#Task 11
import custom_module
def set_that_secret(str):

    custom_module.set_secret(str)

set_that_secret("Tiger")
print(custom_module.secret)

#Task 12
def read_minutes():
    minutes1 = {}
    minutes2 = {}
    rows = []
    with open('../csv/minutes1.csv', 'r') as file:
        reader = csv.reader(file)
        minutes1["fields"] = next(reader)

        for row in reader:
            rows.append(tuple(row))
        minutes1["rows"] = rows


    rows = []
    with open('../csv/minutes2.csv', 'r') as file:
        reader = csv.reader(file)
        minutes2["fields"] = next(reader)

        for row in reader:
            rows.append(tuple(row))
        minutes2["rows"] = rows


    return minutes1,  minutes2
    
minutes1, minutes2 = read_minutes()
#print (minutes1)
#print (minutes2)

#Task 13
def create_minutes_set():
    #turn the rows into a set for minutes1 and minutes2
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])
    #combine thwo sets into one set(union)
    combine_set = minutes1_set.union(minutes2_set)
    #return the set
    return combine_set

create_minutes_set()
minutes_set = create_minutes_set()
#print(minutes_set)
#Task 14
from datetime import datetime
def create_minutes_list():
    minutes_list= list(minutes_set)
#covert the list elements into a tuple
#convert each tuple's second element into datatime object
    
    result_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return result_list

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    result_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open('./minutes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        for row in result_list:
            writer.writerow(row)
    return result_list
write_sorted_list()