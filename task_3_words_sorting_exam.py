def words_sorting(*args):
    dict_words = {}
    for word in args:
        word_chars_sum = 0
        for char in word:
            word_chars_sum += ord(char)
        dict_words[word] = word_chars_sum
        if sum(dict_words.values()) % 2 == 0:
            sorted_dict = sorted(dict_words.items(), key=lambda x: x[0])
        elif sum(dict_words.values()) % 2 != 0:
            sorted_dict = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for item in sorted_dict:
        result += f'{item[0]} - {item[1]}\n'
        result.strip()

    return result


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#     ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#     ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
