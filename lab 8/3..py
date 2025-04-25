
names = set()


names.add("Alice")
names.add("Bob")
names.add("Charlie")
names.add("Diana")
names.add("Eve")

print("Set after adding five names:", names)


if "Charlie" in names:
    names.remove("Charlie")
    names.add("Carlos")

print("Set after modifying one name:", names)


names.discard("Alice") 
names.discard("Eve")

print("Set after deleting two names:", names)

