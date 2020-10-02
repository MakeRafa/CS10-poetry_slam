
# This is a new python file
# random library
import random
filename = "poem.txt"
# gets the filename poem.txt and moves it here

def get_file_lines(filename):
    read_poem = open(filename, 'r')
# reads the poem.txt file 
    return read_poem.readlines()

def lines_printed_backwards(lines_list):
    lines_list = lines_list[::-1] #this reverses a line
    for line in lines_list: #this is used in every function afterwards to pick poem lines
        print(line)

print("*************************************************************************")

print("Backwords Poem")


lines_printed_backwards(get_file_lines(filename)) # calling the function to be able to print

print("*************************************************************************")


def lines_printed_random(lines_list):
    random.shuffle(lines_list) #mixes lines in random order
    for line in lines_list:
        print(line)

print("Random Line Poem")

lines_printed_random(get_file_lines(filename))

print("*************************************************************************")

print("Every 5th line Poem")

# def lines_printed_custom():
with open('poem.txt') as fifth:
    for num, line in enumerate(fifth): 
        if num%5 == 0: #chooses every fifth line starting at the first one
            print(line)



print("*************************************************************************")