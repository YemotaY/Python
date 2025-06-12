x = input("Press enter :")
print("Enter has the value : " + str(x))
print("x has the type : " + str(type(x)))

if(x==''):
    print("Enter was pressed.")
    exit()
else:
    print("Escape sequence init.")

y = input("Press anything else")
print("Enter has the value : " + str(y))
print("x has the type : " + str(type(x)))