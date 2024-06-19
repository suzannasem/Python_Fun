def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s[0:2].isalpha(): # first two characters letters
        return False
    elif len(s) < 2 or len(s) > 6: # length between 2 and 6
        return False
    elif not s.isalnum(): # contains punctuation
        return False
    elif not numbers(s):
        return False
    elif not zeros(s):
        return False
    else:
        return True

# new function to check if 1st num is zero
def zeros(s):
    # for each char in string
    for i in s: # here i is a character in string

        # store the first numeric char
        first_num = None

        # break out of for loop once we find 1st number
        if i.isnumeric():
            first_num = i
            break

    # check if first_num is zero
    if first_num == '0':
        return False
    else:
        return True


# new function to check for numbers in middle
def numbers(s):

    # test variable: allows for even one instance of num,char to return false
    j = 0

    # loop for next condition
    for i in range(len(s)-1): # here i is a number representing list position

        # if i is numeric and i+1 is alpha, add to j
        if s[i].isnumeric() and s[i+1].isalpha():
            j += 1

    # tests if j has changed
    if j > 0:
        return False
    else:
        return True

main()
