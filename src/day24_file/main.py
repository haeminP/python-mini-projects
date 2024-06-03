# file = open("my_file.txt")

# default mode is read
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("I like pasta!")

# file.close()


