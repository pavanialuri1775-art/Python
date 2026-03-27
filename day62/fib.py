#fibonacci sequence:is the sum of the two preceding ones. 
#We can use recursion to find a specific number in the sequence
#ex:Find the 7th number in the Fibonacci sequence.
def fibonacci(n):
      if n <= 1:
        return n
      else:
       return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))#13'''

#recursion with lists
#Recursion can be used to process lists by handling one element at a time.
#ex:Calculate the sum of all elements in a list.
def sum_list(numbers):
      if len(numbers) == 0:
        return 0
      else:
        return numbers[0] + sum_list(numbers[1:])
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

#find the maximum value in a list:
def find_max(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest
my_list=[3,7,2,9,1]
print(find_max(my_list))