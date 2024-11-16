name = input("Enter Name Of Student : ")
roll = int(input("Enter Roll Number :"))
MM = int(input("Enter Maximum Marks :"))
M1 = int(input("Enter Marks In Data Structure : "))
M2 = int(input("Enter Marks In DS & TOL :"))
M3 = int(input("Enter Marks In COA : "))
M4 = int(input("Enter Marks In Engineering Mathematics-IV :"))
M5 = int(input("Enter Marks In Technical Communication :"))
Total = M1 + M2 + M3 + M4 + M5
Avg = Total / 5
Status = "Pass"
if Avg <= 40.0:
    Status = "Fail"

fp = open("ReportCard.txt", "w")
fp.write("Name : " + name + "\n")
fp.write("Roll.No. : " + str(roll) + "\n")
fp.write("----------------------------------------------------------------\n")
fp.write("----------------------------------------------------------------\n")
fp.write("Subject\t\t\t\t\t\t\t\t\t\t Maximum Marks\t\t\t\t\t\t\t\t\t\tObtained Marks\n")
fp.write("----------------------------------------------------------------\n")
fp.write("Data Structure\t\t\t\t\t\t\t\t\t"+str(MM)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(M1)+"\n")
fp.write("COA\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(MM)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(M3)+"\n")
fp.write("DS & TOL\t\t\t\t\t\t\t\t\t\t\t\t"+str(MM)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(M2)+"\n")
fp.write("Engineering Mathematics-IV\t\t\t"+str(MM)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(M4)+"\n")
fp.write("Technical Communication \t\t\t\t"+str(MM)+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(M5)+"\n")
fp.write("----------------------------------------------------------------\n")
fp.write("----------------------------------------------------------------")
fp.write("\n\n\n\n\n")
fp.write("Total Obtained Marks : " + str(Total) + "\n")
fp.write("Percentage : " + str(Avg) +"%\n")
fp.write("Result : "+Status)
