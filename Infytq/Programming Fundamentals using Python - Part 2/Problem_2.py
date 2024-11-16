#lex_auth_0127135773590405121141

def bracket_pattern(st):
    ls=[]
    for ch in st:
        if ch=='(':
            ls.append(ch)
        elif len(ls)==0 and ch==')':
            return False
            
        elif ch==')':
            ls.pop()
    if len(ls)==0:
        return True
    return False
    

    
input_str=input("Enter String: ")
print(bracket_pattern(input_str))