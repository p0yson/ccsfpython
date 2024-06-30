def main():
    pints = []
    get_pints(pints)
    #total_pints
    #average_pints
    #high_pints
    #low_pints

def get_pints(pints):
    for i in range(7):
        user_pints = int(input('Enter pints collected: '))
        pints.append(user_pints)

    return pints

main()