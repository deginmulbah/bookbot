from stats import get_num_words
from stats import get_char_diction
from stats import sort_char_diction
import sys

def get_book_text(path):
    with open(path, "r") as file: 
        file_content = file.read()
    return file_content

def main():
    args_list = sys.argv
    
    if(len(args_list) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_content = get_book_text(args_list[1])
    words_count = get_num_words(file_content.split())
    char_diction = get_char_diction(file_content)
        
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    sort_char_diction(char_diction)
    print("============= END ===============")
    
main()