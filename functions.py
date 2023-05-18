

def alternate_caps(string):
    """
    Returns a string with alternate letters capitalized
    """
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 1:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    return new_string




