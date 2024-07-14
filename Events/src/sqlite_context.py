import json
import sqlite3
from datetime import datetime as dt

class Connection:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute_file(self, filepath):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()

        file = open(filepath, "r")
        sql = file.read()
        file.close()

        commands = sql.strip().split(";")

        processed = {"success": [], "fail": []}

        for command in commands:
            try:
                cursor.execute(command)
                processed["success"].append(command)
            except sqlite3.Error as e:
                error = {"command": command,
                        "error": str(e)}
                processed["fail"].append(error)
                return json.dumps(processed)

        con.close()
        return json.dumps(processed)

    def track_event(self, username, source_id, payload):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()

        processed = {"success": [], "fail": []}
        command = "INSERT INTO events (updated_by, source_id, payload) VALUES (?, ?, ?)"

        try:
            con.execute("BEGIN TRANSACTION")
            cursor.execute(command, (username, source_id, payload))
            processed["success"].append(command)
            con.commit()
        except sqlite3.Error as e:
            con.rollback()
            error = {"error": str(e),
                    "command": command}
            processed["fail"].append(error)

        con.close()
        return json.dumps(processed)

    def process_event(self, username, row_id):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()

        processed = {"success": [], "fail": []}
        command = "UPDATE events SET processed = TRUE WHERE id = ? or source_id = ?"

        try:
            # Start a transaction
            con.execute("BEGIN TRANSACTION")

            # Track the event (insert tracking entry)
            insert_result = self.track_event(username, row_id, command)
            processed["success"].append(insert_result)

            # Execute the update command
            cursor.execute(command, (row_id, row_id))
            processed["success"].append(command)

            # Commit the transaction if everything was successful
            con.commit()

        except sqlite3.Error as e:
            # Rollback the transaction on error
            con.rollback()

            error = {"error": str(e), "command": command}
            processed["fail"].append(error)

        con.close()
        return json.dumps(processed)


    def cancel_event(self, username, row_id):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()

        processed = {"success": [], "fail": []}
        command = "UPDATE events SET cancelled = TRUE WHERE id = ? or source_id = ?"

        try:
            # Start a transaction
            con.execute("BEGIN TRANSACTION")

            # Track the event (insert tracking entry)
            insert_result = self.track_event(username, row_id, command)
            processed["success"].append(insert_result)

            # Execute the update command
            cursor.execute(command, (row_id, row_id))
            processed["success"].append(command)

            # Commit the transaction if everything was successful
            con.commit()

        except sqlite3.Error as e:
            # Rollback the transaction on error
            con.rollback()

            error = {"error": str(e), "command": command}
            processed["fail"].append(error)

        con.close()
        return json.dumps(processed)


    def query_rows(self, statement):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()

        cursor.execute(statement)
        rows = cursor.fetchall()
        con.close()

        return rows


if __name__ == "__main__":
    test_db = Connection("/home/mason/Public/Events/test/test.db")
    filepath = "sql/initial.sql"

    created = test_db.execute_file(filepath)
    tracked = test_db.track_event("mason", None, created)

    row_id = 1
    processed_row = test_db.process_event("mason", row_id)
    cancelled_row = test_db.cancel_event("mason", row_id)

    print(test_db.query_rows("SELECT * FROM events"))

