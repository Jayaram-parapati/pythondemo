# Sample objects with key-value pairs
object1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
object2 = {'name': 'Bob', 'age1': 25, 'city': 'Los Angeles'}

# Specify the keys you want to compare
key_to_compare = ['age','age1']

# Access the values associated with the keys in each object
value1 = object1.get(key_to_compare)
value2 = object2.get(key_to_compare)

# Compare the values using comparison operators
if value1 is not None and value2 is not None:
    if value1 < value2:
        print(f"{object1['name']}'s {key_to_compare} is less than {object2['name']}'s {key_to_compare}.")
    elif value1 > value2:
        print(f"{object1['name']}'s {key_to_compare} is greater than {object2['name']}'s {key_to_compare}.")
    else:
        print(f"{object1['name']}'s {key_to_compare} is equal to {object2['name']}'s {key_to_compare}.")
else:
    print(f"One of the objects doesn't have the key '{key_to_compare}'.")
