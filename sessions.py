# Module for functions to manipulate data from WorkoutSessions Table
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

def check_session(session_id):  # function to validate if workout session already exists (DONE)
    conn = connect_database()
    try:
        cursor = conn.cursor()
        query = "SELECT 1 FROM WorkoutSessions WHERE id = %s"
        cursor.execute(query, (session_id, ))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
                
# Function to add workout session to database
def add_session(session_id, member_id, date, duration_min, calories_burned):
    conn = connect_database()
    try:
        cursor = conn.cursor()
        new_session = (session_id, member_id, date, duration_min, calories_burned) 
        if check_session(session_id):
            print('Session already exists.')
        else: 
            query = "INSERT INTO WorkoutSessions(id, member_id, date, duration_min, calories_burned) VALUES(%s, %s, %s, %s, %s)"
            cursor.execute(query, new_session)
            conn.commit()
            print("New Session added to workouts.")
    except Exception as e:   # Error handling for invalid member ID or other constraints
        print(f"Error: {e}") 
    finally:
        cursor.close()
        conn.close()  

# Function to remove workout session from database
def delete_session(session_id):
    conn = connect_database()
    try:
        cursor = conn.cursor()
        session_to_remove = session_id
        if check_session(session_to_remove):
            query = "DELETE FROM WorkoutSessions WHERE id = %s"
            cursor.execute(query, (session_to_remove, ))
            conn.commit()
            print("Workout Session Deleted.") 
        else:
            print("Workout Session not found.")     
    except Exception as e: 
        print(f"Error: {e}")  
    finally:
        cursor.close()
        conn.close() 

# Function to display Workout Sessions table (DONE) 
def fetch_sessions():
    conn = connect_database()
    try:
        cursor = conn.cursor()       
        query = "SELECT * FROM WorkoutSessions"        
        cursor.execute(query)        
        for session in cursor.fetchall():
            print(session)
    except Exception as e: 
        print(f"Error: {e}") 
    finally:
        cursor.close()
        conn.close() 
        