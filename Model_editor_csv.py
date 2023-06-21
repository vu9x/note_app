from Model_Note import Note

class editor_scv:

    @classmethod
    def read_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
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
    def write_csv(cls):
        pass
