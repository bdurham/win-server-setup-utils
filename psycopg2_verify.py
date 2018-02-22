import psycopg2
import sys

# database specific connection properties
db_server = r'ec2-35-169-118-17.compute-1.amazonaws.com'
db_database = r'd560e5pi2h4prd'
db_user = r'ITW'
db_pass = r'p2491b9618451541cf49e0f995dc9c83e33197ed4bf2e3a5bf9cffc83fe9fd7ce'
db_port = r'5432' # default PostgreSQL port

# build connection string
db_connection = list()
db_connection.append(f'host={db_server}')
db_connection.append(f'dbname={db_database}')
db_connection.append(f'user={db_user}')
db_connection.append(f'password={db_pass}')
db_connection.append(f'port={db_port}')

# establish connection
db_connection_str = ' '.join(db_connection)
print(f'Connection string: {db_connection_str}')
conn =  psycopg2.connect(db_connection_str)
cursor = conn.cursor()
cursor.execute('select * from groups')
print(cursor.description)
for col in cursor.description:
    print(col.name)

for row in cursor:
    # print(row)
    pass

# cleanup
cursor.close()
conn.close()
sys.exit()

