import csv

customers_file = open('customers.csv','r')
reader = csv.reader(customers_file)


customer_country_file = open('customer_country.csv','w')
writer = csv.writer(customer_country_file, delimiter = ' ')
for column in reader:
    writer.writerow((column[1],column[2],column[4]))
    
