from sys import argv

# variables to hold the user input argument
script, filename = argv

# open file as per user input from terminal and hold in txt variable
txt = open(filename)

# print filename and it's content
print("Here's your file %r: " % filename)
print(txt.read())

# # Enter the filename to read
# print("Enter the filename again: ")
# file_again = input("> ")
#
# # open file as per user input and hold in txt_again variable
# txt_again = open(file_again)
#
# # print the content in the text file
# print(txt_again.read())
