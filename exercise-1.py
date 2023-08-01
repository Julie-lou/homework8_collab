
numbers = [1, 2, 3, 4]
def replace_last(numbers):
    for x in numbers:
        numbers.append(numbers.pop(0))
        numbers.append(numbers.pop(0))
        numbers.append(numbers.pop(0))

        return numbers
    
print (replace_last(numbers))




