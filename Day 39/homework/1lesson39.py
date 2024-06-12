def duplicate_encode(word):
    new_word = word.lower()
    result = ""
    for char in new_word:
        if new_word.count(char) > 1:
            result += ")"
        else:
            result += "("
    return  result

print(duplicate_encode(input()))