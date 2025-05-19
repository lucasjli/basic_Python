import random
from collections import Counter

# Generate a list of 100 random integers between 1 and 50, store in a list
num = list(random.choices(range(1, 51), k=100))
# Using Counter to calculate integers and their frequencies, dictionary format: key, value
count_dict = Counter(num)

top3_reversed = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:3]

for num, frequency in top3_reversed:
    print(f"{num} occurs {frequency} times")
