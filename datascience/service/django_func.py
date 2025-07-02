def str_to_int(s):
    """
    Converts a string to an integer.
    :param s: String to convert
    :return: Integer value of the string
    """
    try:
        return int(s)
    except ValueError:
        raise ValueError(f"Cannot convert {s} to an integer.")

def create_logger(argument=5):
    with open("django_func.log", "w") as f:
        f.write(f"This is a placeholder for the django_func.log file.{argument}\n{str_to_int('440')}\n")
