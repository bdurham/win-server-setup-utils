import psycopg2
import psycopg2.extras
import sys

'''
Execute groups of statements in fewer server roundtrips
http://initd.org/psycopg/docs/extras.html

psycopg2.extras.execute_batch(cur, sql, argslist, page_size=100)

Semantically similar to, but much faster than

cur.executemany(sql, argslist)

Different implementation: Psycopg will join the statements into fewer
multi-statement commands, each one containing at most page_size statements,
resulting in a reduced number of server roundtrips.

Note: Does not update cursor.rowcount property.

Note execute_batch() can be also used in conjunction with PostgreSQL
prepared statements using PREPARE, EXECUTE, DEALLOCATE.

Instead of executing:

execute_batch(cur, "complex SQL with %s %s params", params_list)

Use prepared statements which may bring further performance benefits.
If the operation to perform is complex, every single execution will be faster
as the query plan is already cached; furthermore the amount of data to send
on the server will be lesser (one EXECUTE per param set instead of the whole,
likely longer, statement).

cur.execute("PREPARE stmt AS complex SQL with $1 $2 params")
execute_batch(cur, "EXECUTE stmt (%s, %s)", params_list)
cur.execute("DEALLOCATE stmt")

Fast bulk inserts and updates
http://initd.org/psycopg/docs/extras.html

psycopg2.extras.execute_values(cur, sql, argslist, template=None, page_size=100)

'''

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
# cursor that returns name tuplies, row[0] or row.column
# http://initd.org/psycopg/docs/extras.html
db_connection_str = ' '.join(db_connection)
print(f'Connection string: {db_connection_str}')
conn =  psycopg2.connect(db_connection_str, cursor_factory=psycopg2.extras.NamedTupleCursor)

cursor = conn.cursor()
cursor.execute('select * from groups')
print(cursor.description)
for col in cursor.description:
    print(col.name)

for counter, row in enumerate(cursor):
    if counter > 10:
        break
    print(counter, row.id, row.updated_at)

# cleanup
cursor.close()
conn.close()
sys.exit()

