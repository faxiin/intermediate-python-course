import random

# fixed errors (indentation and function name)


def dice_sum(die_size, rolls):
    results = 0
    dice_sum = 0
    for i in range(0, rolls):
        results = random.randint(1, die_size)
        print("Die %d rolled %d." % (i+1, results))
        dice_sum += results
    print("Total of %d dice rolls is: %d" % (rolls, dice_sum))
    # return the result of your calculation instead of `None`
    return dice_sum


# get user input (you might think about catching errors)
die_size = int(input('What is the size of your die? [enter a #]'))
rolls = int(input('How many would you like to roll? [enter a #]'))

# pass input values to function and print result
result = dice_sum(die_size=die_size, rolls=rolls)
print(result)
