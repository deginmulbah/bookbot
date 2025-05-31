def get_num_words (words): 
    return len(words)

def get_char_diction (word): 
    char_diction = {}
    
    for char in word:
        lower_case_char = char.lower()
        if lower_case_char in char_diction:
            char_diction[lower_case_char] = char_diction[lower_case_char] + 1
        else:
            char_diction[lower_case_char] =  1
                    
    return char_diction

def sort_char_diction(char_diction):
    sorted_dict = dict(sorted(char_diction.items(), key=lambda item: item[1], reverse=True))
    for char in sorted_dict: 
        count = sorted_dict[char]
        if(char.isalpha()):
            print(f"{char}: {count}")
    