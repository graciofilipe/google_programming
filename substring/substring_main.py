#https://techdevguide.withgoogle.com/resources/find-longest-word-in-dictionary-that-subsequence-of-given-string/?programming_languages=python#!
def find_substring(mega_string, set_of_words):
    pass

def check_if_word_is_substring(mega_string, word):
    if len(word) > len(mega_string):
        return False
    elif word == mega_string:
        return True
    else:
        ct = 0
        for letter_1 in word:
            for letter_2 in mega_string:
                if letter_1 == letter_2:
                    mega_string = mega_string[1:]
                    ct += 1
                    if ct == len(word):
                        return True
                    break
                else:
                    mega_string = mega_string[i + 1:]

    return False



x = check_if_word_is_substring('anbpdflhkjedf', 'aple')
print(x)