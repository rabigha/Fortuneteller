x = input("Enter a color (Blue, Red, Black, or Orange): ")

if x == "Blue":
    a = int(input("Input a number from 1-10: "))
    if a <= 5:
        print("You will live with the person love.")
    elif a > 10:
        print("Invalid")
    else:
        print("You will be single.")

elif x == "Red":
    b = int(input("Input a number from 11-20: "))
    if b <= 15:
        print("You will live in a mansion!")
    elif b > 20:
        print("Invalid input")
    else:
        print("You will live in an apartment.")

elif x == "Black":
    c = int(input("Input a number from 21-30: "))
    if c <= 25:
        print("You will have 2 children.")
    elif c > 30:
        print("Invalid input")
    else:
        print("You will have no children.")

elif x == "Orange":
    d = int(input("Input a number from 31-40: "))
    if d <= 35:
        print("You will have a pet.")
    elif d > 40:
        print("Invalid input")
    else:
        print("You will have 5 pets.")

else:
    print("Invalid Input")
