import csv

customers_file = open('customers.csv','r')
reader = csv.reader(customers_file)
for item in reader:
    print(item)

customer_country_file = open('customer_country.csv','w')
print(customer_country_file)




#cc = open('customer_country.csv', 'w')
#cc.write('Customer Name','Customer Country')
