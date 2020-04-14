#Lesson 101

mylist = ["a","b","c","d"]

new_string = ''
for x in range(10):
    for c in mylist:
        new_string += c+", "
    print(new_string)
