list = {
     "a" : "00001",
     "b" : "00011",
     "c" : "00111",
     "d" : "01111",
     "e" : "11111",
}
while True:
    user_input = input("enter a letter or string: ")

    for i in user_input:
        if user_input in list:
            print(f"{user_input} is on the list")
        else:
            print(f"{user_input} is not in list")  