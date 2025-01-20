def main():
    print("--- Begin report of books/frankenstein.txt ---")

    book = get_book_text("books/frankenstein.txt")
    #print(book)
    print(f"{get_word_count(book)} words found in the document\n")
    for k, v in get_character_count(book).items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    return 0

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def get_word_count(text):
    words = text.split()
    return len(words)
    
def get_character_count(text):
    char_dictionary = {}
    book = list(text.lower())
    for char in book:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1        

    sorted_char = dict(sorted(char_dictionary.items(), key=lambda item: item[1], reverse=True))

    return sorted_char

main()