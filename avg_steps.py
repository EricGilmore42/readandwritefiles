import csv

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w', newline = '')

reader = csv.reader(infile, delimiter = ',')

next(reader)

writer = csv.writer(outfile, delimiter = ',')


count = '0'

for row in infile: 
    if row[0] == '1':
        writer.writerow('January')
        while row[0] == '1':
            count += row[1]
        writer.writerow(count)
    
outfile.close()

