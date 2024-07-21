#!/usr/bin/env python3
import json
import sqlite3
from datetime import datetime as dt

class Connection:
    def __init__(self, db_path):
        self.db_path = db_path

    def setup(self):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()
        return (con, cursor)

    def execute_file(self, filepath):
        con, cursor = self.setup()

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

        con.close()
        return json.dumps(processed)

    def create_event(self, table_name, username, payload):
        con, cursor = self.setup()

        command = f"INSERT INTO {table_name} (created_by, payload) VALUES (?, ?)"

        output = {}

        try:
            con.execute("BEGIN TRANSACTION")
            cursor.execute(command, (username, payload))
            con.commit()

            output ={"command": command,
                    "payload" : payload}
        except sqlite3.Error as e:
            con.rollback()
            output = {"error": str(e),
                    "command": command}

        con.close()
        return json.dumps(output)

    def process_event(self, table_name, username, row_id):
        con, cursor = self.setup()

        command = f"UPDATE {table_name} SET processed = TRUE, updated_by = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?"

        output = {}

        try:
            con.execute("BEGIN TRANSACTION")
            cursor.execute(command, (username, row_id))
            con.commit()

            output ={"command": command}
        except sqlite3.Error as e:
            con.rollback()
            output = {"error": str(e),
                    "command": command}

        con.close()
        return json.dumps(output)

    def cancel_event(self, table_name, username, row_id):
        con, cursor = self.setup()

        command = f"UPDATE {table_name} SET cancelled = TRUE, updated_by = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?"

        output = {}

        try:
            con.execute("BEGIN TRANSACTION")
            cursor.execute(command, (username, row_id))
            con.commit()

            output ={"command": command}
        except sqlite3.Error as e:
            con.rollback()
            output = {"error": str(e),
                    "command": command}

        con.close()
        return json.dumps(output)

    def get_unprocessed(self, table_name):
        con, cursor = self.setup()

        statement = f"SELECT * FROM {table_name} WHERE processed = FALSE ORDER BY created_at ASC"

        cursor.execute(statement)
        rows = cursor.fetchall()
        con.close()

        return rows

    def query_table(self, statement):
        con, cursor = self.setup()

        cursor.execute(statement)
        rows = cursor.fetchall()
        con.close()

        return rows


if __name__ == "__main__":
    test_db = Connection("../test/test.db")
    filepath = "sql/initial.sql"
    table_name = "events"
    username = "mason"

    created = test_db.execute_file(filepath)
    tracked = test_db.create_event(table_name, username, created)


    row_id = 1
    processed_row = test_db.process_event(table_name, username, row_id)
    cancelled_row = test_db.cancel_event(table_name, username, row_id)

    rows = test_db.query_table(f"SELECT * FROM {table_name}")

    print(rows)
