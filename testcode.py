import pymysql

connection=pymysql.connect(
    host="localhost",
    user='root',
    password='root',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)
try:
    with connection.cursor() as cursor:
        create_query="""
        create table if not exists employees(id int auto_increment primary key,
        name varchar(50),
        department varchar(10)
        );
        """
        cursor.execute(create_query)
        insert_query="insert into employees (name,department) values(%s,%s)"
        values=[('pradeep','cse'),('kishore','cse'),('elaks','cse')]
        cursor.executemany(insert_query,values)
        connection.commit()

        select_query="select * from employees"
        cursor.execute(select_query)
        result=cursor.fetchall()
        with open("Empoyes_db.txt",'w')as f:
            for row in result:
                f.write(f"{row}\n")

finally:
    connection.close()