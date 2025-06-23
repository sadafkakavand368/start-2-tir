print("Hello ladies and gentlemans welcome to the Sara's birthday!!")
print("please add your name: ")
Name = input()
if Name in ["Victor", "Tom", "Lia", "Ian", "Rose"]:
    print("Welcome to the party" +  Name)
    print("")
    print("which foods do you want to choose?")
    print("Hamburger? ghormesabzi? pizza? kebab? dolme?")
    Foods = input()
    print("okay, thanks! I'll order your foods in a seconds...")
    print("now! here your delicious" + Foods )
    print("my collegues will help you more!...")
    print("bye bye!")
elif Name == "Sara":
    print("honey, you're the host!")
    print("please enjoy your birthday")
else:
    print("oh! I'm so sorry but you're not a guest!")
