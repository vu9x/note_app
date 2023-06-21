import csv
from datetime import datetime

class Note:
    Note_list = []

    #Note constructor
    def __init__(self, id: int, header: str, body: str, created_at, modified_at):
        self.id = id
        self.header = header
        self.body = body
        self.created_at = created_at
        self.modified_at = modified_at

    #Add the note to the class list
    Note.Note_list.append({
        "id": self.id,
        "header": self.header,
        "body": self.body,
        "created_at": self.created_at,
        "modified_at": self.modified_at
    })

    def id(self):
        self.id = Note.Note_list.index(self) + 1

    def created(self):
        self.created_at = datetime.now()

    def modified(self):
        self.modified_at = datetime.now()

    def __str__(self):
        message = f"create: {self.created_at}\n" \
                  f"las modify: {self.modified_at}\n" \
                  f"id: {self.id}\n" \
                  f"header: {self.header}\n" \
                  f"body: {self.body}"

        print(message, "_" * 10)

    def __repr__(self):
        return f"id: {self.id}, {self.header}"