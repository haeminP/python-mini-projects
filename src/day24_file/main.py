# file = open("my_file.txt")
# file.close()


# default mode is read
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write mode
with open("my_file.txt", mode="w") as file:
    file.write("I like pasta!")

# append mode
with open("my_file.txt", mode="a") as file:
    file.write("\nBy the way, I'm Haemin!")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)



