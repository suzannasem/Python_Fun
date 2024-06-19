# define function
def coke():

    # while loop

    j = 0 # initialize: how much money inserted

    while j < 50: # cost of coke is 50 cents
        coin = int(input("Insert Coin:"))
        if coin == 25 or coin == 10 or coin == 5:
            # update j
            j = j + coin
            if j < 50:
                # return amount due (50 - input sums)
                print("Amount Due:", 50 - j)
            elif j >= 50:
                print("Change Owed:", j - 50)
        else:
            print("Amount Due:", 50 - j)
            coin = int(input("Insert Coin:"))

coke()
