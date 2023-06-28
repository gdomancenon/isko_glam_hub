import sqlite3

db_path = 'glms.db'

# This function connects to the DB and returns a conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# This function returns glams by glam_type
def read_glams_by_glam_type(glam_type):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM glam WHERE glam_type = ?'
    value = glam_type
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function retrieves 1 glam by glam_id
def read_glam_by_glam_id(glam_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM glam WHERE id = ?'
    value = glam_id
    result = cur.execute(query,(value,)).fetchall()
    conn.close()
    return result

# This function inserts 1 glam data
def insert_glam(glam_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO glam (glam_type, name, date_established, location, description, url) VALUES (?,?,?,?,?,?)'
    values = (glam_data['glam_type'], glam_data['name'],
              glam_data['date_established'], glam_data['location'],
              glam_data['description'], glam_data['url'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

# This function updates a record
def update_glam(glam_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE glam SET glam_type=?, name=?, date_established=?, location=?, description=?, url=? WHERE id = ?"
    values = (glam_data['glam_type'], glam_data['name'],
              glam_data['date_established'], glam_data['location'],
              glam_data['description'], glam_data['url'],
              glam_data['glam_id'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

