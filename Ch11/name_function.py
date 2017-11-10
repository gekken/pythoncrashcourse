def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = "{} {} {}".format(first, middle, last)
    else:
        full_name = "{} {}".format(first, last)
    return full_name.title()
