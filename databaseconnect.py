import csv
import MYSQLdb
mydb=MYSQLdb.connect(host='localhost',user='root',passwd="Govindu@123",db="test")
curs=mydb.cursor()
csv_data=csv.reader(file('customer_account_info'))
for row in csv_data:
    curs.execute('insert into customer_account_info(account_key,\
          primary_party_key, acct_open_date )' \
          'VALUES("%s", "%s", "%s")',row)
mydb.commit()
curs.close()
print("Done")
