def permute_select(remaining, path=""):  # path: the selected characters; remaining: the remaining characters
    if len(remaining) == 0:  # When 'remaining' is empty, it means the permutation is complete
        print(path)
        return  # Jump back to the previous recursive call

    for i in range(len(remaining)):  # Iterate through the remaining characters
        permute_select(remaining[:i] + remaining[i + 1:], path + remaining[i])  # Recursively select the next character


permute_select("dog")