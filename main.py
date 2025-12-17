# Main class which will take practice entry and then forward it toh total entries.
class PracticeEntry:
    def __init__(self, date: str, subject: str, count: int, note: str = ""):
        self.date = date        # object ke andar save
        self.subject = subject
        self.count = count
        self.note = note        # optional

        date = input("Date: ")
        subject = input("Subject: ")
        count = input("Count: ")
        note = input("Note: ")
class AllEntries:
    def __init__(self):
        # yaha ek hi baar empty structures bante hain
        self.entries = []   # yaha PracticeEntry objects ki list aayegi
        self.targets = {}   # subject -> target

    def add_entry(self, date: str, subject: str, count: int, note: str = ""):
        """
        Naya PracticeEntry banao aur entries list me daal do.
        """
        for entry in PracticeEntry:
            self.entries.append(entry)
        
         # yaha tu khud logic likhega

    def show_entries(self):
        """
        Saari entries print karne ke liye.
        """
        pass

    # aage chalke: total_by_subject, most_productive_day, etc.
tracker = AllEntries()
entry1 = PracticeEntry("2025-01-15", "python", 8, "loops")
entry2 = PracticeEntry("2025-12-25", "SQL", 5, "Methods") 
tracker.entries.append(entry1)
print(tracker.entries[0].date, tracker.entries[0].subject)