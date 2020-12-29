
"""
1. Create an object which will represent donor (All the values from the google forms trigger)
2. Create a function which will push the donor object to the SQL database.
"""

"""
Maybe consider writing a class for blood type and donations
"""
import pyodbc


class Donor:
    def __init__(self, timestamp, email, name, birthdate, gender, blood_type, donations, phone):
        self.timestamp = timestamp
        self.email = email
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.blood_type = blood_type
        self.donations = donations
        self.phone = phone

    def get_object(self):
        return {
            'timestamp': self.timestamp,
            'email': self.email,
            'name': self.name,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'blood_type': self.blood_type,
            'donations': self.donations,
            'phone': self.phone
        }


# Singleton design pattern
class Database:

    __db_connection = None

    __server_address = 'Donators.mssql.somee.com'
    __database_name = 'Donators'
    __user_ID = 'hadasok_SQLLogin_1'
    __password = 'wm9w7a7698'
    __driver = 'SQL Server'
    __tables_creator_file = './InitializeDB.sql'
    __tables_values_file = './tables_values.sql'

    def get_instance():
        if Database.__db_connection is None:
            # Create the connection
            Database.__db_connection = Database.initial_contact()

        return Database.__db_connection

    def initial_contact():
        db_connection = pyodbc.connect(
            ("DRIVER={};"
            "SERVER={};"
            "DATABASE={};"
            "Trusted_Connection=no;"
            "UID={};"
            "PWD={};").format(
                Database.__driver,
                Database.__server_address,
                Database.__database_name,
                Database.__user_ID,
                Database.__password
            )
        )
        Database.initial_tables(db_connection)
        Database.initial_tables_values(db_connection)

        return db_connection

    def initial_tables(db_connection):
        Database.load_sql_query_file(db_connection, Database.__tables_creator_file)

    def initial_tables_values(db_connection):
        Database.load_sql_query_file(db_connection, Database.__tables_values_file)

    def load_sql_query_file(db_connection, file_name):

        with open(file_name, 'r', encoding='utf-8') as sql_commands:
            commands = sql_commands.read()
            split_commands = commands.split(';')
            split_commands = split_commands[:-1]

            for command in split_commands:
                with db_connection.cursor() as db_cursor:
                    db_cursor.execute(command.replace('\n', ' '))
