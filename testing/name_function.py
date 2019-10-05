def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

def get_formatted_name_v2(first, middle, last):
    full_name = f"{first} {middle} {last}"
    return full_name.title()

def get_full_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"