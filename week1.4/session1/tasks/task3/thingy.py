num = int(input("enter an integer: "))

def spiel(num):
    """
    Function that prints out every even integer between 0 and a specified input integer

    parameters: num, i
    returns: None
    """
    for i in range(0, num + 1):
        if i % 2 == 0:
            print(i)

spiel(num)