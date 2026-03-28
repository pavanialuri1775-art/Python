#find maximum element in a array
def find_max(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        rest_max_element=find_max(numbers[1:])
    return numbers[0] if numbers[0]>rest_max_element else rest_max_element
my_list=[2,1,3,5]
print(find_max(my_list))