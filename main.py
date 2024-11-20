def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(f.name, file_contents)

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

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    list = []
    for key in dict:
        entry = {
            "char": key,
            "count": dict[key]
        }
        list.append(entry)
    return list

def print_report(file_name, file_contents):
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    char_count_list = dict_to_list(char_count)
    char_count_list.sort(reverse=True, key=sort_on)
    print(f'--- Begin report of {file_name} ---\n {word_count} words found in the document\n\n')
    for entry in char_count_list:
        print(f"The '{entry["char"]}' character was found {entry["count"]} times")
    print("--- End report ---")

main()