
# This is a new python file
filename = "poem.txt"

def get_file_lines(filename):
    read_poem = open(filename, 'r')
    return read_poem.readlines()

def lines_printed_backwards(lines_list):
    lines_list = lines_list[::-1]
    for line in lines_list:
        print(line)

lines_printed_backwards(get_file_lines(filename))