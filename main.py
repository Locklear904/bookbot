def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_chars(file_contents))

def count_words(string):
    split_string = string.split()
    total = 0
    for word in split_string:
        total += 1
    return total

def count_chars(string):
    char_dict = {}
    for char in string:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict

main()