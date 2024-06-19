# main function
# conditions for output
    # < 1 = E
    # > 99 = F
    # other = frac*100 %

# function 1: get fraction input
    # call function 2
    # while loop checks for value error and zero division error

# function 2: check input
    # break fraction into x / y
    # are x and y integers?
    # is x < y?

def main():
    j = round(get_frac("Fraction: ")*100)
    if j <= 1:
        print("E")
    elif 99 <= j <= 100:
        print("F")
    else:
        print(f"{j}%")

def get_frac(frac):
    while True:
        try:
            a,b = input(frac).strip().split("/")
            if int(a) <= int(b):
                return int(a)/int(b)
        except (ValueError, ZeroDivisionError):
            pass

main()
