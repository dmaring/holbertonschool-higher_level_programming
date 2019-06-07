#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """

    ret_list = []
    with open(filename, mode='r', encoding="utf-8") as f:
        full_file = f.read()
        file_list = full_file.split('\n')
        for line in range(len(file_list)):
            if line < len(file_list) - 1:
                ret_list.append(file_list[line] + '\n')
            else:
                ret_list.append(file_list[line])
            if search_string in file_list[line]:
                ret_list.append(new_string)

    with open(filename, mode='w', encoding="utf-8") as f:
        ret_string = "".join(ret_list)
        f.write(ret_string)
