import csv

sales_file = open('sales.csv','r')
reader = csv.reader(sales_file)



sales_report_file = open('salesreport.csv','w')
writer = csv.writer(sales_report_file, delimiter=' ')
for column in reader:
    writer.writerow((column[0],column[3]))

