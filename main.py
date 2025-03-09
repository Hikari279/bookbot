import sys
from stats import count_characters
from stats import count_words
from stats import sort_dictionary_into_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    num_chars = count_characters(get_book_text(path))
    num_words = count_words(get_book_text(path))
    sorted_chars = sort_dictionary_into_list(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    print("============= END ===============")

main()
    