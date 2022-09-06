import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)


for record in csvfile:
    salary = float(record[3]) * float(record[4] + 1)
    print('Employee ID: ', record[0])
    print('First Name: ', record[1])
    print('Last Name: ', record[2])
    print('Total Salary: ', str(format(salary,.2)))
    input()
