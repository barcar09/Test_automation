#open a file remve donts and commas, remove non unique words
# sort list of words
open_three_rings = open("three_rings.txt","r")

text_to_file = open_three_rings.read()
open_three_rings.close()

text_to_file = text_to_file.replace(',','')
text_to_file = text_to_file.replace('.','')
text_to_file = text_to_file.split()
text_to_file = sorted(list(set(text_to_file)))
for el in text_to_file:
    print(el)