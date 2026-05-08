def count_unique_words(a):
    word = a.split()
    unique_words_set = set(word)
    return len(unique_words_set)
input= "manish mithran mithran"
unique = count_unique_words(input)
print(f"The number of unique words is: {unique}")
