#1. Accessing

# tup1=('ab', 'bc', 'cd', 'de')

# # Tuple Indexing
# print(tup1[0])

# # Tuple Unpacking
# a,b,c,d=tup1     # No. of variables on left must be equal to No. of items in Tuple  [a,b,c,d,e=tup1 - Error]
# print(a)
# print(b)
# print(c)
# print(d)

#2. Concatenation

# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')

Tuple3 = Tuple1 + Tuple2
Tuple1 = Tuple2 + Tuple3  # No Error
# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)

# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)

# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)
