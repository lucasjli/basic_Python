# Basic Python

# Assignment Goal
* Practice programming in Python3 by completing eight small programming exercises.

## Preamble
1. Fork this repository using the button at the top of the project page.
2. Make sure that the visibility of your project is private. (Settings > expand Permissions > Project visibility: Private; Save changes).  *Note: Class teachers and tutors will still have read access to your project for marking purposes.*
3. Clone the new repository to your computer using Git.  Store the repository in your COMPX575 directory.
4. Remember to commit and push regularly as you work on the project! 

### Exercise One
Generate a list of 100 random integers between 1 and 50 and count the occurrences of each integer. For example, 1 occurs 3 times, 2 occurs 5 times, etc.
### Exercise Two
Write a function that calculates the total cost of items in a cart, represented as a list of dictionaries. Each dictionary has three keys: 'name', 'price', and 'quantity'. Template follows:
```
def calculate_total(cart):
    # code to calculate total cost
    
cart = [{'name': 'banana', 'price': 0.99, 'quantity': 5}, {'name': 'milk', 'price': 1.50, 'quantity': 2}]
print(calculate_total(cart))
# output: 7.95
```
### Exercise Three
Write a program that generates 100 random integers between 1 and 50, and finds the top three integers with the highest occurrences.
### Exercise Four
Use *collections.deque* to reverse the words in the following sentence.
```
The quick brown fox jumps over the lazy dog.
```
Hint: use split() to split a string into a list.
### Exercise Five
Write a program that generates a list that contains 100 random integers between 1 and 50, and a recursive function that returns the smallest number in the list.  You must use recursion for this exercise!
### Exercise Six
Write a recursive function to print out all the combinations of a string.

For example, for the string "dog", it should print the following (in any order):
dog
dgo
odg
ogd
gdo
god

### Exercise Seven
Given the list of student records (in tuples) below,
1. sort the students in a ascending order of age
2. sort the students by surname
```
students = [
    {'id': '1000', 'name': 'Jane Smith', 'age': 20},
    {'id': '1001', 'name': 'John White', 'age': 16},
    {'id': '1002', 'name': 'Alex Brown', 'age': 19},
    {'id': '1003', 'name': 'Mary Johns', 'age': 17}
]

```
### Exercise Eight
Given a sentence (below), write a program that uses *map, reduce and filter* to:
1. Display the words that start with a vowel, e.g., Alice, author.
2. Find the shortest word (including punctuation marks).
3. Uppercase all words in the sentence.
4. Remove all vowels from the sentence.
```
Alice's Adventures in Wonderland (commonly shortened to Alice in Wonderland) is an 1865 novel written by English author Charles Lutwidge Dodgson under the pseudonym Lewis Carroll.
```
Hint: use *split()* to split a string into a list.
## Grading
This task is worth as much as 5% of your final grade and is marked out of 8 (1 mark per exercise).

## Submission
Submit your Python code to your Git repository as well as to Moodle.
