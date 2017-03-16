import sys

print("Hello, Python!")

if True:
    print("True")
else:
    print("False")

file_finish = "done"
file_text = ""
try:
    # open file stream
    file = open("abc.txt", "w")
except IOError:
    print ("There was an error writing to", "abc.txt")
    sys.exit()
print("Enter '", file_finish)
print("' When finished")
while file_text != file_finish:
    file_text = input("Enter text: ")
    if file_text == file_finish:
        # close the file
        file.close
        break
    file.write(file_text)
    file.write("\n")
file.close()

try:
    file = open("abc.txt", "r")
except IOError:
    print ("There was an error reading file")
    sys.exit()
file_text = file.read()
file.close()
print(file_text)

# Mullti line statements
total = "item_one" + \
        "item_two" + \
        "item_three"

# Multiple statements
x = 'foo'; sys.stdout.write(x + '\n')
