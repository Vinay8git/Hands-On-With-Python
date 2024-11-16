#lex_auth_0127135739583692801137

def add_string(str1):
  #start writing your code here
    if len(str1)<3:
        return str1
    if str1[-3:]=="ing":
        str1=str1+"ly"
    elif str1[-3:] != "ing":
        str1=str1+"ing"    
  
    return str1

str1=input("Enter String: ")
print(add_string(str1))