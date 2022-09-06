import csv

infile = open('steps.csv', 'r')

csvfile = csv.reader(infile, delimiter = ',')

outfile = open('avg_steps.csv', 'w')

outfile.write('Month, ' + 'Steps')

jan_total = 0
jan_cnt = 0
feb_total = 0
feb_cnt = 0
mar_total = 0
mar_cnt = 0
apr_total = 0
apr_cnt = 0
may_total = 0
may_cnt = 0
jun_total = 0
jun_cnt = 0
jul_total = 0
jul_cnt = 0
aug_total = 0
aug_cnt = 0
sep_total = 0
sep_cnt = 0
oct_total = 0
oct_cnt = 0
nov_total = 0
nov_cnt = 0
dec_total = 0
dec_cnt = 0

for row in csvfile:
    if row[0] == '1':
        jan_total += int(row[1])
        jan_cnt += 1
    elif row[0] == '2':
        feb_total += int(row[1])
        feb_cnt += 1
    elif row[0] == '3':
        mar_total += int(row[1])
        mar_cnt += 1
    elif row[0] == '4':
        apr_total += int(row[1])
        apr_cnt += 1
    elif row[0] == '5':
        may_total += int(row[1])
        may_cnt += 1
    elif row[0] == '6':
        jun_total += int(row[1])
        jun_cnt += 1
    elif row[0] == '7':
        jul_total += int(row[1])
        jul_cnt += 1
    elif row[0] == '8':
        aug_total += int(row[1])
        aug_cnt += 1
    elif row[0] == '9':
        sep_total += int(row[1])
        sep_cnt += 1
    elif row[0] == '10':
        oct_total += int(row[1])
        oct_cnt += 1
    elif row[0] == '11':
        nov_total += int(row[1])
        nov_cnt += 1
    elif row[0] == '12':
        dec_total += int(row[1])
        dec_cnt += 1

JanAvg = format(jan_total / jan_cnt,'.2f')
FebAvg = format(feb_total / feb_cnt,'.2f')
MarAvg = format(mar_total / mar_cnt,'.2f')
AprAvg = format(apr_total / apr_cnt,'.2f')
MayAvg = format(may_total / may_cnt,'.2f')
JunAvg = format(jun_total / jun_cnt,'.2f')
JulAvg = format(jul_total / jul_cnt,'.2f')
AugAvg = format(aug_total / aug_cnt,'.2f')
SepAvg = format(sep_total / sep_cnt,'.2f')
OctAvg = format(oct_total / oct_cnt,'.2f')
NovAvg = format(nov_total / nov_cnt,'.2f')
DecAvg = format(dec_total / dec_cnt,'.2f')

outfile.write('\nJanuary, ' + str(JanAvg))
outfile.write('\nFebuary, ' + str(FebAvg))
outfile.write('\nMarch, ' + str(MarAvg))
outfile.write('\nApril, ' + str(AprAvg))
outfile.write('\nMay, ' + str(MayAvg))
outfile.write('\nJune, ' + str(JunAvg))
outfile.write('\nJuly, ' + str(JulAvg))
outfile.write('\nAugust, ' + str(AugAvg))
outfile.write('\nSeptember, ' + str(SepAvg))
outfile.write('\nOctober, ' + str(OctAvg))
outfile.write('\nNovember, ' + str(NovAvg))
outfile.write('\nDecember, ' + str(DecAvg))

outfile.close()