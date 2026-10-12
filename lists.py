
marks = [3, 5, 6, "Harry", True]

print(marks)
print(type(marks))

# Positive indexing
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# Negative indexing
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

# Check if an item exists
if 6 in marks:
    print("Yes")
else:
    print("No")

if "Ha" in "Harry":
    print("Yes")

# List slicing
print(marks)
print(marks[1:-1])
print(marks[1:4:2])

print(marks[0:len(marks)])
print(marks[1:9])
print(marks[1:9:3])

if "6" in marks:
    print("Yes")
else:
    print("No")
