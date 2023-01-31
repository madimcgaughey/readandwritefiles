import csv

employee_bonus = open('EmployeePay.csv','r')
bonus = csv.reader(employee_bonus, delimiter = ',')
next(bonus)
for record in bonus:
    print(record)
    print('Employee ID:', record[0])
    print('Employee First Name:', record[1])
    print('Employee Last Name:', record[2])
    print('Salary:',record[3])
    print('Bonus:',record[4])
    input()  


   
