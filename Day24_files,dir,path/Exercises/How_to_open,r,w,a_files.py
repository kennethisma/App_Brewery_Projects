# file_text = open("my_file.txt")

# content = file_text.read()

# print(content)

# file_text.close()


# with open("my_file.txt") as file_txt:
#     content = file_txt.read()
#     print(content)

##########################
with open("my_file.txt", mode="r") as file_txt:  # mode = "r"read,"w"write, "a"append
    file_2 = file_txt.read()
print(type(file_2))
