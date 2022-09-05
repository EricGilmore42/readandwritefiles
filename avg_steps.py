import csv

step_file = 'steps.csv'

infile = open(step_file, 'r')
outfile = open('avg_steps.csv', 'w', newline = '')

reader = csv.reader(infile)

next(reader)

writer = csv.writer(outfile, delimiter = ',')

count = '0'

for row in infile: 
    if row[0] == '1':
        writer.writerow('January')
        while row[0] == '1':
            count += row[1]
        writer.writerow(count)