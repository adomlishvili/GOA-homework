foods = ["apple", "banana", "cherry"]

foods.append("date")
print(foods)              # .append() - სიის ბოლო ქონტში დაამატებს ელემენტს "date"

foods.insert(1, "blueberry")
print(foods)              # .insert() - ინდექს 1-სთან დაასვით "blueberry" სიაში

popped_item = foods.pop()
print(popped_item)        # .pop() - ამოღებს და აბრუნებს სიიდან ბოლო ელემენტს
print(foods)              # სიიდან ბოლო ელემენტი წაიშლება

foods.remove("banana")
print(foods)              # .remove() - წაშლის სიიდან პირველი "banana" ელემენტს
