import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"sqlite.db"

    sql_create_instructors_table = """ CREATE TABLE IF NOT EXISTS instructors (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql_create_courses_table = """ CREATE TABLE IF NOT EXISTS courses (
                                        id integer PRIMARY KEY,
                                        instructor_id INTEGER,
                                        name text NOT NULL,
                                        description TEXT,
                                        FOREIGN KEY (instructor_id) REFERENCES instructors (id)
                                    ); """

    sql_create_announcements_table = """ CREATE TABLE IF NOT EXISTS announcements (
                                        id integer PRIMARY KEY,
                                        course_id INTEGER,
                                        title text NOT NULL,
                                        text TEXT,
                                        timestamp TEXT, 
                                        FOREIGN KEY (course_id) REFERENCES courses (id)
                                    ); """

    sql_create_assignments_table = """CREATE TABLE IF NOT EXISTS assignments (
                                    id integer PRIMARY KEY,
                                    course_id INTEGER,
                                    name text NOT NULL,
                                    description TEXT,
                                    assignment_link TEXT,
                                    FOREIGN KEY (course_id) REFERENCES courses (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create instructors table
        create_table(conn, sql_create_instructors_table)

        # create courses table
        create_table(conn, sql_create_courses_table)

        # create announcements table
        create_table(conn, sql_create_announcements_table)

        # create assignments table
        create_table(conn, sql_create_assignments_table)
        
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()