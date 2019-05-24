import sys
import csv
import pymysql

print('Overtime App by Tyrone')

fname = input('Please insert your first name: ')

while len(fname) == 0:
	if len(fname) == 0:
		fname = input('I repeat, please enter your first name: ')
	else:
		print('Thank you, ', fname)


lname = input('Please insert your last name: ')

print('Thank you ', fname, ' ', lname, ',')
ticknos = input('please insert the ticket numbers you worked on, seperated by a hyphen(-): ')

print('Thank you, ', fname, ' ', lname, ', you have worked on tickets: ', ticknos)

custname = input('Please insert the names of the customers who created these tickets, also seperated by a hyphen: ')

start = input('Please insert your start time as format hh:mm: ')

end = input('Thank you. Lastly, please insert the end time: ')

print('You have entered the following information:')
print('You are: ', fname, ' ', lname)
print('You worked on the following tickets in this session: ', ticknos)
print('Your session started at: ', start,', and ended at: ', end)

line = [[fname, lname, ticknos, custname, start, end]]

decision = input('Can you confirm the above information is correct and it can be written to the file?(Y/N) ')

f = open('output.csv', 'w')

if decision == 'Y':
	with f:
		writer = csv.writer(f)
		writer.writerows(line)
		sys.exit('OT Logged.')
elif decision == 'N':
	print('Cancelling operation...')
	sys.exit('Program closed.')
else:
	sys.exit('Incorrect confirmation provided. Closing.')

def csv_to_mysql(load_sql, host, user, password):
#    '''
#    This function load a csv file to MySQL table according to
#    the load_sql statement.
#    '''
    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)
        print('Connected to DB: {}'.format(host))
        # Create cursor and execute Load SQL
        cursor = con.cursor()
        cursor.execute(load_sql)
        print('Succuessfully loaded the table from csv.')
        con.close()
        
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

# Execution Example
load_sql = """LOAD DATA LOCAL INFILE '/Users/tyroneanderson/Documents/GitHub/Overtime/output.csv'
INTO TABLE Overtime.Overtime FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 0 LINES;"""
host = '127.0.0.1'
user = 'root'
password = 'root'
csv_to_mysql(load_sql, host, user, password)


