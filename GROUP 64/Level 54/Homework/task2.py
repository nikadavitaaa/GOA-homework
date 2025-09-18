def wedge(*Strings):
    Wedged_string = ""
    for string in Strings:
        Wedged_string += string

    return Wedged_string

print(wedge(("Hello" + "Hi")))
