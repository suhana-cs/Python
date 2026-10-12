
def average(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)

def name(**details):
    print("Hello,", details["fname"], details["lname"])

result = average(5, 6, 7, 1)
print("Average is:", result)

name(fname="Alex", lname="Smith")
