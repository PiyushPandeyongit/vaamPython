# tuples are immutable
# ordered
# homogeneous
# used()to create tuples
# example my_tuple=(1,2,3,"hello",true)
# elements can be accesed using their index starting from 0
my_tuple = (1, 2, 3)
my_tuple1 = (4, 5)

# Concatenation
combined_tuple = my_tuple  + my_tuple1  
print(combined_tuple)# Output: (1, 2, 3, 4, 5)

# Repetition
repeated_tuple = my_tuple * 2 
print(repeated_tuple) # Output: (1, 2, 3, 1, 2, 3)

# Length
length = len(my_tuple) 
print(length) # Output: 3

# Membership
is_present = 2 in my_tuple1
print(is_present)  # Output: True

# slicing
sub_mytuple=my_tuple[0:3]
print(sub_mytuple)

