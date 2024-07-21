#!/usr/bin/env python3
from SimpleQueue import SimpleQueue
from SqliteContext import Connection
import json

class EventQueue:
    def __init__(self, db_path, queue_length, table_name):
        self.db_path = db_path
        self.table_name = table_name
        self.queue_length = queue_length
        self.queue = SimpleQueue(self.queue_length)
        self.connection = Connection(self.db_path)

    def load_queue(self):
        rows = self.connection.get_unprocessed(self.table_name)
        for row in rows:
            self.queue.enqueue(row[7])

        return self.queue._list

    def add_event(self, table_name, username, payload):
        self.queue.enqueue(payload)
        self.connection.create_event(table_name, username, payload)

        return self.queue._list



if __name__ == "__main__":
    db_path = "../test/test.db"
    queue_length = 10
    table_name = "events"
    username = "mason"

    queue = EventQueue(db_path, queue_length, table_name)

    loaded = queue.load_queue()
    print(loaded)

    payload = {"create": {"test": "test"}}
    events = queue.add_event("events", "mason", json.dumps(payload))
    print(events)
