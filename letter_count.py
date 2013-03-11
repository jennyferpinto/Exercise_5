from sys import argv
import string

script, filename = argv

open_file = open(filename).read()

az = string.lowercase[:27]

dictionary = dict.fromkeys(az, 0)

     
#new_file = open open_file.read())

# making file lowercase
lowercase_file = open_file.lower()


for char in lowercase_file:
	if char in dictionary:
		dictionary[char] += 1
		break

sorted_list = [x for x in dictionary.iteritems()]
sorted_list.sort(key=lambda x: x[0])

print "\n".join(str(char[1]) for char in sorted_list)
#edited_text = text_editor(open_file)

#a_count = 0
#for char in edited_text:
 #   edited_text.read(1)   
  #  if char == ord('a'):
   #     a_count = a_count + 1
    #else:
     #   continue
    #print a_count
