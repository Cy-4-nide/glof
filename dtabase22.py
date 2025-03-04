import sqlite3

def clear_database():
    conn = sqlite3.connect("glof_data.db")
    cursor = conn.cursor()
    
    # Clear the sensor_data table
    cursor.execute("DELETE FROM sensor_data")
    conn.commit()
    
    print("Database cleared successfully!")
    conn.close()

# Call the function to clear the database
clear_database()
