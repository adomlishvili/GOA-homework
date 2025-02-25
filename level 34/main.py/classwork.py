def manual_map(func, iterable):
    
    result = []
    
    for item in iterable:
        
        result.append(func(item))
    return result


def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = manual_map(square, numbers)
print(squared_numbers)  