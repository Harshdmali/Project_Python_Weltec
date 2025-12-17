class PracticeEntry:
    def __init__(self,date,subject,count,notes):
        self.date = date
        self.subject = subject
        self.count = count
        self.notes = notes
    def display(self):
        date=self.date
        subject= self.subject
        questions= self.count
        notes = self.notes
    def display(self):
        print(f"Date: {self.date} | Subject: {self.subject} | Questions: {self.count} | Notes: {self.notes}")          

entry = PracticeEntry("2025-01-15", "python", 8, "loops practice")
entry.display()