# pylint: disable=missing-docstring

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def add_comma(a_string):
    """
    returns a copy of the string with every word separated by a comma
    example: add_comma("John Peter Jude") => "John, Peter, Jude"
    """
    pass  # YOUR CODE HERE
    words = a_string.split()
    result = ", ".join(words)
    return result


def belongs_to(a_string, a_word):
    """
    returns True if a_string contains a_word
    example: belongs_to("hey jude", "jude") => True
    """
    pass  # YOUR CODE HERE
    words = a_string.split()
    if a_word in words:
        return True
    else:
        return False


def count_repetition(a_string, a_substring):
    """
    returns how many times a_substring occurs in a_string
    example: count_repetition("000123000123", "0") => 6
    """
    pass  # YOUR CODE HERE
    counts = a_string.count(a_substring)
    return counts

def is_a_question(a_string):
    """
    returns True if a_string ends with a "?"
    example: is_a_question("How are you?") => True
    """
    pass  # YOUR CODE HERE
    return a_string.endswith("?")


def remove_surrounding_whitespaces(a_string):
    """
    returns a copy of the string with leading and trailing whitespaces removed
    example: delete_surrounding_whitespaces("  hey yo  ") => "hey yo"
    """
    pass  # YOUR CODE HERE
    return a_string.strip()

def replace(initial_string, old_letter, new_letter):
    """
    returns a copy of the string with the new letter replacing the old one
    example: replace("casanova", "a", "o") => "cosonovo"
    """
    pass  # YOUR CODE HERE
    return initial_string.replace(old_letter, new_letter)

def full_description_concatenation(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using concatenation
    example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
    """
    pass  # YOUR CODE HERE
    return first_name.capitalize() + " " + last_name.capitalize() + " " + "is "+ str(age)

def full_description_formatting(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using string interpolation
    example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
    """
    pass  # YOUR CODE HERE
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"
