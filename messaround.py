def emphasize_n_characters(word, n_chars):
    str = ''
    for i in range(len(word)):
        if i < n_chars:
            str += word[i] + '!'
        else:
            str += word[i]
    return str

print(emphasize_n_characters('watermelon', 5))