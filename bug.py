def function_with_uncommon_bug(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a + b

# This is a test that could cause an exception in some scenarios.
result = function_with_uncommon_bug(0, 0)  # this works
print(result) # prints 0
result = function_with_uncommon_bug(5,0) #this works
print(result) #prints 5
result = function_with_uncommon_bug(0,5) #this works
print(result) #prints 5
result = function_with_uncommon_bug(5,5) #this works
print(result) #prints 10
# However, this might not trigger an exception, depending on the behavior of the interpreter or runtime environment.
# The issue lies in the reliance on implicit type conversion and the potential for unexpected results with specific input types, especially involving zero division or undefined behaviors in non-standard libraries.

# Example with potential for floating-point errors and unexpected behavior:
result = function_with_uncommon_bug(1e-100, 1e100) # possible floating-point errors
print(result)
