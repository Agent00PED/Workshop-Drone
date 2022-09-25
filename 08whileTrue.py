total = 0
while True:
    n = int(input("Enter number : "))
    if n != 0:
        total = total + n
        print("total = ",(total))
    else:
        print (total)
        break
print ("End of process!")