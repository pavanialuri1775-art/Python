#Finding the maximun value
def max_value(*numbers):
    if len(numbers)==0:
        return None
    maximum_value=numbers[0]
    for num in numbers:
        if num>maximum_value:
            maximum_value=num
    return maximum_value
print(max_value(23,44,12,66))#66
print(max_value())   