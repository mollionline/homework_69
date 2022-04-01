
def is_digit(string):
    if string.replace('-', '').isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

