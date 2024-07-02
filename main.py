def word_count(book):
    book_list = book.split()
    return len(book_list)

def char_count(book):
    char_dict = {}
    book = book.lower()
    book_words = book.split()
    for word in book_words:
        for letter in word:
            if letter not in char_dict and letter:
                char_dict[letter] = 1
            else:
                char_dict[letter] = 1 + char_dict[letter]
    
    return char_dict


path = "books/frankenstein.txt"

with open(path, "r") as book:
    book_text = book.read()
    word_c = word_count(book_text)
    letter_c = char_count(book_text)
    letter_c.sort

print(f"---| Char analisys of {path} |---")
for k,v in letter_c.items():
    if k.isalpha():
        print(f"The '{k}' letter was found {v} times.")
    else:
        continue
    
