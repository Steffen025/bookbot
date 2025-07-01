def get_book_text(link):
    """
    Fetches the text content of a book from a given link.
    
    Args:
        link (str): The URL of the book to fetch.
    
    Returns:
        str: The text content of the book.
    """
    with open(link) as file:
        text = file.read()
    return text

from stats import word_count
from stats import char_count
from stats import sort_dict_by_value

def main():
    """
    Main function to print the book statistical report.
    """
    link = "books/frankenstein.txt" 
    book_text = get_book_text(link)
    sorted_char_count = sort_dict_by_value(char_count(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {link}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words.")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

main()

