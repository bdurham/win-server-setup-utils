# capture.py

'''
Verify pyodbc working with Alterra databases.

Features beyond the DB API
https://github.com/mkleehammer/pyodbc/wiki/Features-beyond-the-DB-API
'''

'''

db_user = r'idirectory\malcolm.greene'
db_pass = r'...1'

RTP UAT
VM-DED-SQLC1N1.ILAB.TST\DEV,49733 - RTPIkon

RTP Prod 
VN-DEN-IKONL.idirectory.itw,49733 - RTPOne 

AMP UAT - SQL Server (Informatica replicated AMP PostgreSQL)
VM-DED-SQLC1N1.ILAB.TST\DEV,49733 - EITDev

AMP UAT - PostgreSQL 
User: ITW
Password: p2491b9618451541cf49e0f995dc9c83e33197ed4bf2e3a5bf9cffc83fe9fd7ce
Host: ec2-35-169-118-17.compute-1.amazonaws.com
Database: d560e5pi2h4prd
Port: 5432 

Ref UAT


Ref Prod


AMP Utility UAT
VM-DED-SQLC1N1.ILAB.TST\DEV,49733 - AMPUtility

RDS (dbo.SaleDates, dbo.Meals)
server: udp-powerbi-sandbox.c4yiy3ssz15k.us-west-2.rds.amazonaws.com
database: Sandy
user: udp_powerbi_sandbox_admin
pass: PastrySportAnywhere

'''

import pyodbc
import sys

# TODO: Pull rows in blocks of N-rows via cursor.fetchall( ... )
# TODO: Be friendly to production source and pull reasonable sized blocks of records
def test_table_pull(cursor):
    sql_command = 'select *, 456 as JOB_ID from dbo.TransactionHeader'
    cursor.execute(sql_command)
    
    print(cursor.description)
    for col in cursor.description:
        print(col[0])
        
    for row in cursor:
        # print(row.transactionid, row.job_id)
        pass


# pull a table, save it to disk as a CSV
def pull_table(table_name, job_id):
    sql_command = f'select *, {job_id} as job_id from {table_name}'
    cursor.execute(sql_command)

    col_names = [col[0] for col in cursor.description]
    print(col_names)

    '''    
    print(cursor.description)
    for col in cursor.description:
        print(col[0])
        
    for row in cursor:
        # print(row.transactionid, row.job_id)
        pass
    '''
    

# if you are running on Windows, you can just use the native driver: driver={SQL Server}

db_driver = '{ODBC Driver 13 for SQL Server}'
db_driver = '{SQL Server}'

# database specific connection properties
db_server = r''
db_database = r''
db_user = r''
db_pass = r''
db_app = r'message visible to SQL Server admin'

db_server = r'VM-DED-SQLC1N1.ILAB.TST\DEV,49733'
db_database = r'RTPIkon'

# build connection string
db_connection = list()
db_connection.append(f'driver={db_driver}')
db_connection.append(f'server={db_server}')
db_connection.append(f'database={db_database}')
db_connection.append(f'trusted_connection=yes')
# db_connection.append(f'uid={db_user}')
# db_connection.append(f'pwd={db_pass}')

'''
# RDS sandbox tests
db_server = r'udp-powerbi-sandbox.c4yiy3ssz15k.us-west-2.rds.amazonaws.com'
db_database = r'Sandy'
db_user = r'udp_powerbi_sandbox_admin'
db_pass = r'PastrySportAnywhere'
db_connection = list()
db_connection.append(f'driver={db_driver}')
db_connection.append(f'server={db_server}')
db_connection.append(f'database={db_database}')
db_connection.append(f'uid={db_user}')
db_connection.append(f'pwd={db_pass}')
'''


# establish connection
db_connection_str = '; '.join(db_connection)
print(f'Connection string: {db_connection_str}')

conn = pyodbc.connect(db_connection_str)

# treats all column names as lowercase for row.column references
pyodbc.lowercase = True
cursor = conn.cursor()
cursor.fast_executemany = True

# test pull
# pull_table()

'''
# RDS sandbox tests
sql_command = f'select * from dbo.Meals'
sql_command = f'select * from dbo.SaleDates'
cursor.execute(sql_command)
for row in cursor:
    print(row)
'''

# cleanup
cursor.close()
conn.close()
sys.exit()




