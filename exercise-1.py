def replace_last(numbers):
    if len(numebers) <= 1:
        return numbers
    else:
        numbers[0] = number[-1]
        numbers.remove(number[-1])
        return numbers
    ...
