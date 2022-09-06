import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)


for record in csvfile:
    print('Student ID: ', record[0])
    print('First Name: ', record [1])
    print('Last Name: ', record[2])
    print('City: ', record[3])
    print('Country: ', record[4])
    print('Phone: ', record[5])
    input()
