import sys
import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

upper_letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# range start at 0 and ends at 5
for i in range(6):
  print(i)
sys.exit()

# to count to 10, you must end at 11
print("when printing a range from 1 to 10, then range end must be 11")
range_start = 0
range_end = 11
print(f"range_start: {range_start}, range_end: {range_end}")
for i in range(range_start, range_end):
  print(f"i is {i}")

#sys.exit()


len_numbers = len(numbers)
range_start = 0
print(f"range_start: {range_start}, range_end/len_numbers: {len_numbers}")
for i in range(range_start, len_numbers):
  print(f"i is {i}")

#sys.exit()

print()
range_start = 0
range_end = 10
print(f"range_start: {range_start}, range_end: {range_end}")
for i in range(0,10):
  print(f"i is {i}")

print()
my_list = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" ]
print(f"my_list has {len(my_list)} elements")
for i in range(0, len(my_list)):
  print(f"{i} - index {i} is {my_list[i]}")

print()
range_start = int(input("Enter a starting number: "))
range_end = int(input(f"Enter how many numbers to print starting at {range_start}: ")) + range_start
print(f"range_start: {range_start}, range_end: {range_end}")
for i in range(range_start, range_end):
  print(f"i is {i}")