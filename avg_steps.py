import csv

infile = open('steps.csv', 'r')
csvfile = csv.reader(infile, delimiter=',')
outfile = open('avg_steps.csv','w')

next(csvfile)
outfile.write('Month, Average Steps\n')

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
dec_count = 0

for row in csvfile: 
    if int(row[0]) == 1:
        jan_total += int(row[1])
        jan_count += 1
    elif int(row[0]) == 2:
        feb_total += int(row[1])
        feb_count += 1
    elif int(row[0]) == 3:
        mar_total += int(row[1])
        mar_count += 1 
    elif int(row[0]) == 4:
        april_total += int(row[1])
        april_count += 1
    elif int(row[0]) == 5:
        may_total += int(row[1])
        may_count += 1
    elif int(row[0]) == 6:
        june_total += int(row[1])
        june_count += 1 
    elif int(row[0]) == 7:
        july_total += int(row[1])
        july_count += 1
    elif int(row[0]) == 8:
        aug_total += int(row[1])
        aug_total += 1
    elif int(row[0]) == 9:
        sep_total += int(row[1])
        sep_count += 1
    elif int(row[0]) == 10:
        oct_total += int(row[1])
        oct_count += 1
    elif int(row[0]) == 11:
        nov_total += int(row[1])
        nov_count += 1
    elif int(row[0]) == 12:
        dec_total += int(row[1])
        dec_count += 1

    JanAvg = jan_total/jan_count
    FebAvg = feb_total/feb_count
    MarchAvg = mar_total/mar_count
    AprilAvg = april_total/april_count
    MayAvg = may_total/may_count
    JuneAvg = june_total/june_count
    JulyAvg = july_total/july_count
    AugAvg = aug_total/aug_count
    SepAvg = sep_total/sep_count
    OctAvg = oct_total/oct_count
    NovAvg = nov_total/nov_count
    DecAvg = dec_total/dec_count



    outfile.writerow('\nJanuary, ' + str(format(JanAvg), '.2f'))
    outfile.writerow('\nFebuary, ' + str(format(FebAvg), '.2f'))
    outfile.writerow('\nMarch, ' + str(format(MarchAvg), '.2f'))
    outfile.writerow('\nApril, ' + str(format(AprilAvg), '.2f'))
    outfile.writerow('\nMay, ' + str(format(MayAvg), '.2f'))
    outfile.writerow('\nJune, ' + str(format(JuneAvg), '.2f'))
    outfile.writerow('\nJuly, ' + str(format(JulyAvg), '.2f'))
    outfile.writerow('\nAugust, ' + str(format(AugAvg), '.2f'))
    outfile.writerow('\nSeptember, ' + str(format(SepAvg), '.2f'))
    outfile.writerow('\nOctober, ' + str(format(OctAvg), '.2f'))
    outfile.writerow('\nNovember, ' + str(format(NovAvg), '.2f'))
    outfile.writerow('\nDecember, ' + str(format(DecAvg), '.2f'))


    outfile.close() 
        