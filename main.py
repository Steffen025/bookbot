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

def main():
    """
    Main function to execute the book statistical analysis.
    """
    link = "books/frankenstein.txt"  # Example file path
    book_text = get_book_text(link)
    print(f"{word_count(book_text)} words found in the document.")
    print(char_count(book_text))

main()