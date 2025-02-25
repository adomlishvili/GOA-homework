umbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)


names = ["Alice", "Bob", "Charlie"]
greetings = list(map(lambda name: "Hello, " + name, names))
print(greetings)



fruits = ["apple", "banana", "kiwi"]
lengths = list(map(len, fruits))
print(lengths)