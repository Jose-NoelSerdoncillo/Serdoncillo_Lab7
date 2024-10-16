name=input(" Enter your Name: ")
section=input(" Enter your Section: ")

pregrade=float(input(" Enter your Preliminary Period Grade: "))
if pregrade > 40 and pregrade < 100:
    print()
else: print("Error")
midgrade=float(input(" Enter your Midterm Period Grade: "))
if midgrade > 40 and midgrade < 100:
    print()
else: print("Error")
finalpgrade=float(input(" Enter your Final Period Grade: "))
if finalpgrade > 40 and finalpgrade < 100:
    print()
else: print("Error")


pregrade * 33.33
midgrade * 33.33
finalpgrade * 33.33 

fgrade= (pregrade + midgrade + finalpgrade)
avg=fgrade/3
finalgrade = round(avg)

if finalgrade>=99 and finalgrade<=100:
    print("1.00")
    print(f"{finalgrade}")
elif finalgrade>=96 and finalgrade<=98:
    print("1.25")
    print(f"{finalgrade}")
elif finalgrade>=93 and finalgrade<=95:
    print("1.50")
    print(f"{finalgrade}")
elif finalgrade>=90 and finalgrade<=92:
    print("1.75")
    print(f"{finalgrade}")
elif finalgrade>=87 and finalgrade<=89:
    print("2.00")
    print(f"{finalgrade}")
elif finalgrade>=84 and finalgrade<=86:
    print("2.25")
    print(f"{finalgrade}")
elif finalgrade>=81 and finalgrade<=83:
    print("2.50")
    print(f"{finalgrade}")
elif finalgrade>=78 and finalgrade<=80:
    print("2.75")
    print(f"{finalgrade}")
elif finalgrade>=75 and finalgrade==77:
    print("3.00")
    print(f"{finalgrade}")
else:print("Failed")