st = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11}
print(st)
s = {2, 4, 6, 8}
st.remove(5)
print(st)
st.add(5)
st.add(6)
print(st)
# st.discard(6)
st.discard(7)
print(st)
print(st & s)
print(st | s)
print(st - s)
print(st ^ s)
# Remove causes error if the element is not present

if s.issubset(st):
    print(True)
if st.issuperset(s):
    print(True)

print(s.symmetric_difference(st))
print(st.symmetric_difference(s))
