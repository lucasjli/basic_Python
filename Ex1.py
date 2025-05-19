import random
from collections import Counter

# Generate a list of 100 random integers between 1 and 50, store in a list
num = list(random.choices(range(1, 51), k=100))
# Using Counter to calculate integers and their frequencies, dictionary format: key, value
count_dict = Counter(num)

for num, frequency in count_dict.items():
    print(f"{num} occurs {frequency} times")