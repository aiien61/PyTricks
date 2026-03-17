import random
from icecream import ic

# randomly generate a number in between 0 and 1
ic(random.random())

# randomly generate an integer in between given integer arguments a and b 
ic(random.randint(1, 5))

# randomly generate a floating number in between given arguments a and b
ic(random.uniform(1, 5))

# randomly generate a number based on a normal distribution with mean mu and standard deviation sigma
ic(random.normalvariate(0, 1))

# random generate a number based on a gamma distribution
ic(random.gammavariate(3, 1))

# randomly generate a number in between numbers of a sequence
ic(random.choice([1, 2, 3, 4, 5]))

# randomly generate given number of items from a population
ic(random.sample([1, 2, 3, 4, 5], 2))

# randomly arrange the order of the given sequence
old_seq = [1, 2, 3, 4, 5]
ic(old_seq)
random.shuffle(old_seq)
new_seq = old_seq
ic(new_seq)


