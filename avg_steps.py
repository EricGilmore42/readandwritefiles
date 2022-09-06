import csv

infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w', newline = '')

reader = csv.reader(infile, delimiter = ',')

next(reader)

writer = csv.writer(outfile, delimiter = ',')

jan_total = 0
jan_count = 0
feb_total = 0
feb_count = 0 
mar_total = 0
mar_count = 0
april_total = 0
april_count = 0
may_total = 0
may_count = 0
june_total = 0
june_count = 0
july_total = 0
july_count = 0
aug_total = 0
aug_count = 0
sep_total = 0
sep_count = 0
oct_total = 0
oct_count = 0
nov_total = 0
nov_count = 0
dec_total = 0
dev_count = 0

