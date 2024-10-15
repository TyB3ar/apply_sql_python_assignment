# Module for functions to maniulate data from Members Table
import mysql.connector
from mysql.connector import Error

def connect_database():
    # Database connection parameters
    db_name = 'database_name'
    user = 'user'
    password = 'password'
    host = 'host'

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
         )
        if conn.is_connected():  
            return conn 
        else:
            print("Could not connect.")
    except Error as e:
        print(f"Error : {e}")
        return None    
        
def check_member(member_id):  # function to validate if member_id already exists (DONE)
    conn = connect_database()
    try:
        cursor = conn.cursor()
        query = "SELECT 1 FROM Members WHERE id = %s"
        cursor.execute(query, (member_id, ))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
    
# Function to add member to database (DONE) 
def add_member(member_id, member_name, member_age):
    conn = connect_database()
    try:    
        cursor = conn.cursor()          
        if check_member(member_id): # validate if member id is already in Members
            print("Member ID already exists.")
        else: # if not in Members
            new_member = (member_id, member_name, member_age) 
            query = "INSERT INTO Members(id, name, age) VALUES(%s, %s, %s)"  
            cursor.execute(query, new_member)
            conn.commit()
            print(f"{member_name} successfully added.")     
    except mysql.connector.Error as db_error:
        print(f"Database error: {db_error}")                     
    except Exception as e:   
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()  

# Function to update member information
def update_member(member_id, new_age):
    conn = connect_database()
    try:
        cursor = conn.cursor()
        if check_member(member_id):
            update_member = (new_age, member_id)
            query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(query, update_member)
            conn.commit() 
            print(f"Member age has been updated.")
        else:
            print("Member ID not found.")
    except mysql.connector.Error as db_error:
        print(f"Database Error: {db_error}")
    except Exception as e:  
        print(f"Error: {e}") 
    finally:
        cursor.close()
        conn.close() 
    
# Function to display Members table (DONE)
def fetch_members():
    conn = connect_database()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM Members'    
        cursor.execute(query)
        for member in cursor.fetchall():
            print(member)           
    except Exception as e:   
        print(f"Error: {e}") 
    finally:
        cursor.close()
        conn.close() 
        