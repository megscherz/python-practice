# Whiteboarding Questions 1

# Be sure to follow the process outlined in the cheat sheet!

# Easy:
# 1. Write a method that returns an array of every number from 1 to 100. 

def a100():
        return list(range(1,101))
# print(a100())

# 2. Write a method that returns an array of every other number from 1 to 100. (That is, 1, 3, 5, 7 … 99)

def a100():
        return list(range(1,101,2))
# print(a100())

# 3. Write a method that returns an array of all numbers from 1 to 1000 that are divisible by 3.

def mults_of_3():
        return list(a for a in range(1,1001) if a % 3 == 0)
# print(mults_of_3())

# 4. Write a method that accepts one argument - an array of numbers - and returns an array of all numbers from that original array that are greater than 7. For example, if the input is [5, 8, 1, 7, 9, 10], the function should return [8, 9, 10].

def greater_7(nums):
        return list(a for a in nums if a >= 7)
test = [5, 8, 1, 3, 7, 10]
# print(greater_7(test))

# 5. Write a method that accepts an array of numbers as a parameter, and returns the number of how many 55’s there are in the array. For example, if the input is [55, 4, 7, 55, 9, 1, 55, 2, 3, 55, 0], the output should be 4. 

def fifty_fives(nums):
        return nums.count(55)
test = [55, 4, 7, 55, 9, 1, 55, 2, 3, 55, 0]
# print(fifty_fives(test))

# 6. Write a method that accepts an array of numbers and returns the sum of the numbers. For example, if the input is [1, 5, 7, 9, 2, 0], the output should be 24.

def sum_of_arr(nums):
        return sum(nums)
test = [55, 4, 7, 55, 9, 1, 55, 2, 3, 55, 0]
# print(sum_of_arr(test))

# name = input("Give me your name:")
# print("Hi, " + name)
# age = int(input("How old are you?"))
# year = 2021 - age + 100
# print(name + ", you will be 100 years old in the year " + str(year))

num = int(input("Give me a number:"))
if num % 2 == 0: 
        print("Your number is even.")
else:
        print("Your number is odd.")

