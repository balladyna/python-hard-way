people = 30
cars = 40
trucks = 40

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
if trucks > cars:
    print("That's to many trucks.")
elif cars > trucks:
    print("Maybe we could take trucks.")
else:
    print("We still can't decide.")
    
if people > trucks:
    print("Alright, let's just take a trucks.")
else:
    print("Fine, let's stay home then.")