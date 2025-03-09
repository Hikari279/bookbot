def count_words(string):
    count = len(string.split())
    return count

def count_characters(string):
    char_count = {}

    for char in string:
        lowered = char.lower()
        if (lowered in char_count):
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1

    return char_count

def sort_dictionary_into_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
