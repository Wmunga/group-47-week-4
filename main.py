AI code
def sort_list_of_dicts(data, sort_key):
    """
    Sorts a list of dictionaries by the specified key.

    Args:
        data (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: x.get(sort_key, 0))

my code
def sort_list_of_dicts(data, sort_key):
    """
    Sort a list of dictionaries by a specific key in a simple, readable way.
    """
    def get_sort_value(item):
        if sort_key in item:
            return item[sort_key]
        else:
            return 0  # Default value if key is missing

    sorted_list = sorted(data, key=get_sort_value)
    return sorted_list
