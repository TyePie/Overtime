import sys
import pymysql

from flask import Flask, render_template, request

app = Flask(__name__)

mysql = pymysql

host = '127.0.0.1'												#Update login details to match your MySQL host details
user = 'root'
password = 'root'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        first_name = details['fname']
        last_name = details['lname']
        ticket_numbers =  details['ticknos']
        customer_names = details['custname']
        start_time = details['start']
        end_time = details['end']
        try:
            con = pymysql.connect(host=host,
                user=user,
                password=password,
                autocommit=True,
                local_infile=1)
            print('Connected to DB: {}'.format(host))
        # Create cursor and execute Load SQL
            cur = con.cursor()
            cur.execute("INSERT INTO Overtime.Overtime(first_name, last_name, ticket_numbers, customer_names, start_time, end_time, created_at) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)", (first_name, last_name, ticket_numbers, customer_names, start_time, end_time))
            cur.close()
            return 'success'
        except Exception as e:
            print('Error: {}'.format(str(e)))
            sys.exit(1)
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
