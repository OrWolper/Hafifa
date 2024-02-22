import psycopg2

class DbConnection:
    def __init__(self, host, dbname, user, password, sslmode):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.sslmode = sslmode
    
    def create_connection(self):
        # Construct the connection string
        conn_string = f"host={self.host} dbname={self.dbname} user={self.user} password={self.password} sslmode={self.sslmode}"

        # Connect to the database
        try:
            conn = psycopg2.connect(conn_string)
            print("Connected to database successfully!")

            return conn
        except Exception as e:
            print(f"Unable to connect to the database: {e}")

    def get_projects_names(self):
        conn = self.create_connection()

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT subsystemname FROM sub_systems")
            rows = cursor.fetchall()
            projectList = []

            for row in rows:
                projectList.append(row[0].lower())
                
            cursor.close()
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()

        return projectList
    
    def get_system_id(self, sysName):
        conn = self.create_connection()
        sysId = None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT sysid FROM systemmapping WHERE LOWER(sysname) = LOWER(%s)", (sysName,))
            sysId = cursor.fetchone()[0]
            cursor.close()
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()

        return sysId

    def get_project_id(self, sysId):
        conn = self.create_connection()
        projectId = None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT subsystemid FROM sub_systems WHERE %s = ANY(sysid)", (sysId,))
            projectId = cursor.fetchone()[0]
            cursor.close()
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()

        return projectId

    def add_new_key(self, sysId, projectId, key):
        conn = self.create_connection()

        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO keys_mapping (sysid, projectid, key) VALUES (%s, %s, %s)", (sysId, projectId, key))
            conn.commit()
            print("New subscription key added successfully!")
            cursor.close()
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()
