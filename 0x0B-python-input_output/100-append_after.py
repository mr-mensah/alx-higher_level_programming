#!/usr/bin/python3
"""Search and append """


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts text after each line containing a given string in a file
    """

    text = ""
    with open(filename) as a:
        for line in a:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
