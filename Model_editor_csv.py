import csv
from Model_Note import Note

class editor_scv:
    path = "path to the file"
    @classmethod
    def read_file(cls):
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            notes = list(reader)

        for note in notes:
            Note(
                id=note.get('id'),
                header=note.get('header'),
                body=note.get('body'),
                created_at=note.get('created_at'),
                modified_at=note.get('modified_at')
            )

    @classmethod
    def save_file(cls):
        with open(path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'header', 'body', 'created_at', 'modified_at'])
            writer.writeheader()
            writer.writerows(Note)

