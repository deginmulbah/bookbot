def get_book_text(path):
    with open(path, "r") as file: 
        file_content = file.read()
    return file_content

def main():
    file_content = get_book_text("./books/frankenstein.txt")
    print(file_content)
    
main()