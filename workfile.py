""" Database setup for program """
from pathlib import Path
# from main import database_data

# global variables
ORIGINAL_DATA_LIST = [['000001', 'Joe Figueroa', '00001', '3269', 'c', '0.00'],
                      ['000002', 'Joe Figueroa', '00001',
                          '3269', 'd', '126000000.00'],
                      ['000003', 'Joe Figueroa', '00001',
                          '3269', 'b', '126000000.00'],
                      ['000004', 'Mia Startan', '00002', '1111', 'c', '0.00'],
                      ['000005', 'Mia Startan', '00002', '1111', 'd', '100000.00'],
                      ['000006', 'Mia Startan', '00002', '1111', 'b', '100000.00'],
                      ['000007', 'Kendo Maximus', '00003', '2222', 'c', '0.00'],
                      ['000008', 'Kendo Maximus', '00003',
                          '2222', 'd', '5632540.00'],
                      ['000009', 'Kendo Maximus', '00003',
                          '2222', 'b', '5632540.00'],
                      ['000010', 'Peluche Mushi', '00004', '1234', 'c', '0.00'],
                      ['000011', 'Peluche Mushi', '00004', '1234', 'd', '50200.00'],
                      ['000012', 'Peluche Mushi', '00004', '1234', 'b', '50200.00'],
                      ['000013', 'Joe Figueroa', '00001', '3269', 'w', '7000.00'],
                      ['000014', 'Joe Figueroa', '00001',
                          '3269', 'b', '125993000.00'],
                      ['000015', 'Papito Main', '00006', '9568', 'c', '0.00'],
                      ['000016', 'Joe Figueroa', '00001', '3269', 'w', '7000.00'],
                      ['000017', 'Joe Figueroa', '00001',
                          '3269', 'b', '125986000.00'],
                      ['000018', 'Mia Startan', '00002', '1111', 'd', '100000.00'],
                      ['000019', 'Mia Startan', '00002', '1111', 'b', '200000.00'],
                      ['000020', 'Kendo Maximus', '00003', '2222', 'd', '10000.00'],
                      ['000021', 'Kendo Maximus', '00003',
                          '2222', 'b', '5642540.00'],
                      ['000022', 'Joe Figueroa', '00001', '3269', 'd', '1000.00'],
                      ['000023', 'Joe Figueroa', '00001',
                          '3269', 'b', '125987000.00'],
                      ['000024', 'Jack Ripper', '00007', '0666', 'c', '0.00'],
                      ['000025', 'Pedro Master', '00008', '2514', 'c', '0.00']]

DATABASE_FILE_NAME = "fakebank_db.txt"


def create_data_line(data):
    """ Create the data line for storage """
    line = ''

    for part in data:
        line = line + part + "\t"

    line = line + "\n"
    return line


def loading_database(database_file):
    """ Loading all data from the Database file """
    print('Loading data ...')
    with open(database_file, 'r', encoding="utf-8") as dbfile:
        database_data = dbfile.read()
        return database_data


def create_database():
    """ Create Database if not found """
    database_file = Path(DATABASE_FILE_NAME)
    if database_file.exists():
        print(f"Database '{database_file}' exists.")

    else:
        print(f"Database '{database_file}' does not exist.")
        print('Creating Database ...')
        with open(database_file, 'w+', encoding="utf-8") as db_file:
            for user_info in ORIGINAL_DATA_LIST:
                db_file.write(create_data_line(user_info))
            print('Database Created.')


def save_database_info(info):
    """ Save a new data line to the database """
    database_file = Path(DATABASE_FILE_NAME)
    with open(database_file, 'a', encoding="utf-8") as db_file:
        db_file.write(info)


def get_database_info():
    """ Get all data from the Database """
    database_data = loading_database(Path(DATABASE_FILE_NAME))
    return database_data
