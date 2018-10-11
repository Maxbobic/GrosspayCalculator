sEmployeename = str(input("please enter the employees name"))
sGender = str(input("please enter the employees gender"))
dHoursworked = float(input("hours worked"))
dPayrate = float(input("payrate"))
dGrosspay = dHoursworked * dPayrate

print(sEmployeename + " is a " + sGender)
print(sEmployeename + " has worked " + str(dHoursworked) + " hours")
print(sEmployeename + "'s payrate is $%.2f" % dPayrate + " a hour")
print(sEmployeename + "'s grosspay is $%.2f" % dGrosspay)
