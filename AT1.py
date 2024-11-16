# st=input("Enter String: ")
# letr=0
# dig=0
# for i in range(len(st)):
#     if(st[i].isalpha()):
#         letr+=1
#     elif st[i].isdigit():
#         dig+=1
# print("Number of letters",letr)
# print("Number of digits",dig)

# st=input("Enter String: ")
# if len(st)<3:
#     print(st)
#     exit()
# if st[-3:]=="ing":
#     print(st+"ly")
# else:
#     print(st+"ing")

# def lstr(lst):
#     max=len(lst[0])
#     for i in range(1,len(lst)):
#         if(len(lst[i])>max):
#             max=len(lst[i])
#     return max
#
# st=input("Enter String List: ")
# lst=st.split(" ")
# print(lst)
# print(lstr(lst))

# def run_len(st):
#     substr=""
#     c=1
#     for j in range(0, len(st)-1):
#         if st[j]==st[j+1]:
#            c += 1
#         else:
#             substr = substr + str(c) + st[j]
#             c = 1
#
#     substr = substr + str(c) + st[-1]
#     return substr
#
# st = input("Enter String: ")
# print(run_len(st))

# from itertools import groupby
# st=input("Enter: ")
# for k,g in groupby(st):
#     print(list(g))
#     print("%d%s"%(len(list(g)),k),end="")


# 1-30 sep
# st=input("Enter String: ")
# if len(st)<2:
#     print("Not Valid")
#     exit()
# print((st[-2:])*4)

# #2-30 sep
# st=input("Enter Sentence: ")
# lt=st.split(" ")
# max,ind=0,0
# for i in range(len(lt)):
#     if len(lt[i])>max:
#         max=len(lt[i])
#         ind=i
#         st=lt[i]
# print("The Maximum Length Word Is ",st," Present At Index ",i," And Length = ",max)

# 3-30sep
# st=input("Enter String: ")
# if len(st)<2 :
#     print("Empty String")
#     exit()
# print(st[:2]+st[-2:])

# 4-30sep
# st=input("Enter String: ")
# c=st[0]
# s=st[0]
# for i in range(1,len(st)):
#     if st[i]==c:
#         s=s+'$'
#     else:
#         s=s+st[i]
# print(s)

# 5-sep30
# s1=input("Enter String1")
# s2=input("Enter String 2")
# tm1=s1[:2]
# tm2=s2[:2]
# s2 = s2.replace(tm2,tm1,2)
# s1 = s1.replace(tm1,tm2,2)
# print(s1+s2)

# lex_auth_012693797166096384149

def find_leap_years(given_year):
    list_of_leap_years = []
    year = given_year
    while (True):
        if (given_year % 4 == 0 and (given_year % 400 == 0 or given_year % 100 != 0)):
            lp = given_year
            break
        else:
            given_year += 1

    for i in range(15):
        list_of_leap_years.append(lp)
        lp += 4
    # Write your logic here

    return list_of_leap_years


list_of_leap_years = find_leap_years(1684)
print(list_of_leap_years)
