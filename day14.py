# Create a tuple of 5 numbers and print it
t1 = (1, 2, 3, 4, 5)
print("Tuple:", t1)

# Access the second element of the tuple
print("Second element:", t1[1])

# Find the length of the tuple
print("Length:", len(t1))

# Check if the number 10 is in the tuple
if 10 in t1:
    print("10 is in the tuple")
else:
    print("10 is not in the tuple")

# Print all elements using a for loop
print("All elements:")
for i in t1:
    print(i)

# Try to change the first element of the tuple (will raise an error)
try:
    t1[0] = 100
except TypeError as e:
    print("Error:", e)

# Concatenate two tuples
t2 = (6, 7)
result = t1 + t2
print("Concatenated tuple:", result)

# Create a tuple with one item and print its type
single_item = (10,)
print("Single-item tuple type:", type(single_item))

# Count how many times a number appears in a tuple
t3 = (1, 2, 2, 3, 2)
print("Count of 2:", t3.count(2))

# Find the index of a specific element in a tuple
print("Index of 3 in t3:", t3.index(3))
