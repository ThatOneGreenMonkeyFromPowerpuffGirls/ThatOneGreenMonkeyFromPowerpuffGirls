class RecordType():
    def __init__(self, theID, theLastName, theFirstName, theDept):
        self.id = the id
        self.lastName = theLastName
        self.firstName = theFirstName
        self.dept = theDept

record1 = RecordType(2468, "Jones", "John", 243)

print(record1.lastName)
record2 = RecordType(1231, "Stevens", "Legnend", 2313)
print(record2.lastName)

people = [
    RecordType(2468, "Jones", "John", 243),
    RecordType(1231, "Stevens", "Legnend", 2313)
]

