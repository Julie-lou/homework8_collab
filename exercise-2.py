
<<<<<<< Updated upstream
=======
numbers = [2, 3, 4, 1]
def index_power(numbers, n):
    for x in numbers:
        if n in range(len(numbers)):
            y = numbers[n]*numbers[n]
            return y
        elif n not in range(len(numbers)):
            return -1

print(index_power([1, 2], 3))
>>>>>>> Stashed changes



