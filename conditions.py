print("rules that govern the state of water")
# let the user pick a temp, see what happens to water (conditional statements)
# current_temp is the tempature veriable (user inputs this)
current_temp = False

while current_temp is False:
    current_temp = input("Enter a tempature: \n")
    print(current_temp)

    # if its below 0, obvi its frozen
    if(int(current_temp) < 0) or (int(current_temp == 0)):
        print("water is a solid. icy!")
        current_temp = False

    # if its between 0 and 100, its liquid
    elif(int(current_temp) < 100):
        print("water is a liquid. ouuuu wet!")
        current_temp = False

    # if its above 100, obvi its a gas
    elif(int(current_temp) > 100) or (int(current_temp == 100)):
        print("water is a vapour. cuz its HOT!")
        current_temp = False
