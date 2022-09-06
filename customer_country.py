import csv 

infile = open('customers.csv','r')

outfile = open('customer_country.csv','w', newline = '')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

outfile.write('Full Name' + ', ' + 'Country' + '\n')

counter = 1 

for record in csvfile: 
    outfile.write(record[1] + ' ' + record[2] + ', ')
    outfile.write(record[4])
    outfile.write('\n')
    counter += 1 

outfile.close() 

print('Customers read from file:', counter)