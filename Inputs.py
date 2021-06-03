
while True:
    try:
        x = input("Please input age: ")
        int(x)
    except:
        print("Age input invalid")
    else:
        break
print("Your age is " + x)
