
##############Absolute path###################
# with open("/Users/Dell/Desktop/my_file.txt") as my_file:
#     content = my_file.read()
#     print(content)

############## Relative path ###################

with open("../../../../../../my_file.txt") as my_file:  # I moved the file to the Desktop
    content = my_file.read()
    print(content)
