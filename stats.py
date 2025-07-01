def word_count(text):
    """
    Counts the number of words in the given text.
    
    Args:
        text (str): The text to count words in.
    
    Returns:
        int: The number of words in the text.
    """

    return len(text.split())

def char_count(text):
    """
    Counts the number of any given character in the text.

    Args:
        text (str): The text to count characters in.

    Returns:
        dictionary: A dictionary containing the character and its count.
    """

    use_text = str.lower(text)
    char_check = []
    char_count_dict = {}

    for char in use_text:
        if char not in char_check:
            char_check.append(char)
            char_count_dict[char] = use_text.count(char)
    return char_count_dict

def sort_dict_by_value(d):
    """
    Sorts a dictionary by its values in descending order.
    
    Args:
        d (dict): The dictionary to sort.
    
    Returns:
        list: A list of tuples sorted by value in descending order.
    """
    
    return sorted(d.items(), key=lambda item: item[1], reverse=True)

