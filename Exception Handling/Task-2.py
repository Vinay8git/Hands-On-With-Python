dic = {"Name": "Vinay", "Gender": "Male", "Roll": 50}
try:
    key = input("Enter")
    print(dic[key])
except Exception as e:
    print("Error : ", e)
