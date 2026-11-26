numbers = (1,4,6,8,10)
# this list comprehension is to filter numbers that are either divisible by 2 or 5 and not by both 2 & 5.
Result = [x  for x in numbers  if (x % 2 == 0) != (x % 5 == 0) ]

print(Result) 

# List comprehension with both Transformation and filtering.
nums = [1, 2, 3, 4, 5]
result = [x * 2 if x % 2 == 0 else x for x in nums if x > 2]
#        [conditional Transformation part]         [Filter condition part]




#List comprehension Questions
numbers = [6,1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))
# 

# Q6. Copying and clearing lists

# Create an independent copy of the original list. Append 50 to the copied list and clear the original list without affecting the copy.

nums = [10, 20, 30, 40]
clist = nums.copy()
nums.clear()

print(nums)
print(clist)
# Q7. Filter even and odd numbers
# Create two separate lists containing even and odd numbers using list comprehension.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = [item for item in nums if item%2 != 0 ]
Even_list = [item for item in nums if item%2 == 0 ]
print(odd_list)
print(Even_list)

# Q8. Square of even numbers
# Create a list containing the squares of only the even numbers.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = [item**2 for item in nums if item%2 != 0]
print(new_list)

# Q9. Conditional replacement
# Replace negative numbers with 0 and retain the remaining numbers using a single list comprehension.
nums = [10, -5, 20, -8, 0, 30, -2]
new_list = [0 if item < 0 else item for item in nums]
print(new_list)
# Q10. String transformation
# Remove leading and trailing spaces, convert names to lowercase and exclude empty strings.
names = ["  Rahul ", "PRIYA", "", " Amit  ", "  ", "NEHA"]
new_list = [item.strip().lower() for item in names if len(item.strip()) > 0  ]
print(new_list)
# Q11. Multiple conditions
# Extract numbers that are divisible by both 3 and 5 from a list of numbers between 1 and 100 (inclusive).
new_list = [item for item in range(0,101) if (item % 3 == 0) and (item % 5 == 0) ]
# new_list = [item for item in range(0,101) if item % 15 == 0 ]
print(new_list)
# Q12. Categorize numbers
# Using a single list comprehension, replace positive numbers with "Positive", negative numbers with "Negative" and zero with "Zero".
nums = [10, -3, 0, 25, -8, 0]
new_list = ['-ve' if item < 0 else '+ve' for item in nums]
print(new_list)
# Q13. Remove duplicates while preserving order
# Remove duplicate elements without changing the original order.
nums = [10, 20, 10, 30, 20, 40, 30, 50]
new_list = []
for i in nums:  
    if (i not in new_list) == True:
        new_list.append(i)
# new_list = list(dict.fromkeys(nums))
print(new_list)

# Q14. Find the second-largest distinct number
# Find the second-largest unique number in the list.
nums = [10, 50, 30, 50, 40, 20]
Second_no = 0
for i in nums:
    if  max(nums)> i> Second_no:
        Second_no = i
print(Second_no)
# Q15. Find the frequency of each element
# Return a list of tuples containing each unique element and its frequency, in order of first appearance.
nums = [10, 20, 10, 30, 20, 10, 40]
for i in nums:
    i = (i,nums.count(i))
    print(i)
print(nums)