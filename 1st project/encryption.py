import random
import string

def encryp(pas):
    chars = string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    cyper = list()

    key = chars.copy()
    random.shuffle(key)

    for letter in pas:
        index = chars.index(letter)
        cyper += key[index]

    return "".join(cyper)