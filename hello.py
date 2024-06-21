text = "Rabbit"
if len(text) > 0:
    print(text[0], end="")
    for i in range(1, len(text)):
        print("-" + text[i], end="")
    print() # to end the line of output