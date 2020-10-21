# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
pets = {}
print ("type 'none' when you want to stop")
while True:
    names = input("What is your pet's name?: ")
    if names == "none":
        break
    types = input ("What is your pet's type (dog, cat, bird)?:")
    if types == "none":
        break
    pets[names]=types
print (pets)
for names, types in pets.items():
    print (names, "is a", types)