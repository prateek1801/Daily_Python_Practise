numbers = (1,4,6,8,10)
# this list comprehension question compares 2 boolean outcomes to make sure that
Result = [x  for x in numbers if (x % 2 == 0) != (x % 5 == 0) ]

print(Result) 

# List comprehension with both Transformation and filtering.
nums = [1, 2, 3, 4, 5]
result = [x * 2 if x % 2 == 0 else x for x in nums if x > 2]
#        [conditional Transformation part]         [Filter condition part]
print(result)