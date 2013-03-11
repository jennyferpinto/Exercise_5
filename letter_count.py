from sys import argv

script, filename = argv

print "Type the filename:"
file_name = raw_input("> ")

open_file = open(file_name)

#1 - i have to make all the strings within the list lowercase

def text_editor(the_text):
    for char in the_text:
        return char
        continue
        str.lower(char)
        
            
edited_text = text_editor(open_file)

a_count = 0
for char in edited_text:
    edited_text.read(1)   
    if char == ord('a'):
        a_count = a_count + 1
    else:
        continue
    print a_count
