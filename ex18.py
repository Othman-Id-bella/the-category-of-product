prix=int(input("enter product price:"))
Cat=input("enter the category of product:")
if Cat=="A":
    print("the total price of the products is:",prix+prix*0.07)
elif Cat=="B":
    print("the total price of the products is:",prix+prix*0.2)
elif Cat=="C":
    print("the total price of the products is:",prix+prix*0.25)
else:
    print("the category does not exist.")