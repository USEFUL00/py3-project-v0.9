import mysql.connector


class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "testuser"            #your user name in db
        self._password = "codequestions"   #your password
        self._database = "db_students"     #put your data base name here
        self.con = None
        self.cursor = None

    def connect_db(self):
        """Establish a connection to the database"""
        self.con = mysql.connector.connect(
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password
        )
        self.cursor = self.con.cursor(dictionary=True)
    
    def add_info(self, id, name, salary, age):
        """Insert a new student record into the database"""
        self.connect_db()

        sql = f"""
            INSERT INTO students_info (id, name, salary, age) 
            VALUES ({id}, '{name}', {salary}, {age});
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
            print("Student added successfully.")  # Debugging
            return None  # No error

        except Exception as e:
            self.con.rollback()
            return e

        finally:
            self.con.close()

    def update_info(self, id, name, salary, age):
        """Update an existing student record in the database"""
        self.connect_db()

        sql = f"""
            UPDATE students_info
            SET name='{name}', salary={salary}, age={age}
            WHERE id={id};
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            return e

        finally:
            self.con.close()

    def delete_info(self, id):
        """Delete a student record from the database"""
        self.connect_db()

        sql = f"""  
            DELETE FROM students_info WHERE id={id};
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            return e

        finally:
            self.con.close()

    def search_info(self, id=None, name=None, salary=None, age=None):
        """Search for student records based on given parameters"""
        self.connect_db()

        conditions = []

        # Add conditions only if fields are not empty
        if id:
            conditions.append(f"id = {id}")  # Exact match for ID
        if name:
            conditions.append(f"name LIKE '%{name}%'")  # Partial match for name
        if salary:
            conditions.append(f"salary LIKE '%{salary}%'")  # Partial match for salary
        if age:
            conditions.append(f"age LIKE '%{age}%'")  # Partial match for age

        # Build the SQL query
        if conditions:
            sql = f"SELECT * FROM students_info WHERE {' AND '.join(conditions)};"
        else:
            sql = "SELECT * FROM students_info;"  # Fetch all records if no condition is given

        print(f"Executing SQL: {sql}")  # Debugging

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print(f"Search result: {result}")  # Debugging
            return result

        except Exception as e:
            return e

        finally:
            self.con.close()
    def get_all_ages(self):
        """Get all distinct ages of students"""

        self.connect_db()

        sql = "SELECT DISTINCT age FROM students_info;"

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as e:
            return e

        finally:
            self.con.close()

    def get_all_salaries(self):
        """Get all distinct salaries of students"""
        self.connect_db()

        sql = "SELECT DISTINCT salary FROM students_info;"

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as e:
            return e

        finally:
            self.con.close()
