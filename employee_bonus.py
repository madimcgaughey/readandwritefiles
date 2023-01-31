import csv

employee_bonus = open('EmployeePay.csv','r')
reader = csv.reader(employee_bonus)
for line in employee_bonus:
    infile = employee_bonus.readlines()
    print(infile)