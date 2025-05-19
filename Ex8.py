import re
from functools import reduce

sentence = "Alice's Adventures in Wonderland (commonly shortened to Alice in Wonderland) is an 1865 novel written by English author Charles Lutwidge Dodgson under the pseudonym Lewis Carroll."


print('1. Display the words that start with a vowel:')
words = re.findall(r"[a-zA-Z]+", sentence)
vowel_words = list(set(filter(lambda word: word[0].lower() in "aeiou", words)))
print(",".join(vowel_words))


print('2. Find the shortest word (including punctuation marks):')
shortest_word_list = []
sentence_list = sentence.split()
min_length = min(map(len, sentence_list))
for word in sentence_list:
    if len(word) == min_length:
        shortest_word_list.append(word)
print(",".join(shortest_word_list))


print('3. Uppercase all words in the sentence:')
upper_sentence = sentence.upper()
print(upper_sentence)


print('4. Remove all vowels from the sentence:')
result = reduce(lambda acc, char: acc + char if char.lower() not in "aeiou" else acc, sentence, "")
print(result)

