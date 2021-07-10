# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.read().split()

# Replace the [name] placeholder with the actual name.
for name in names:
    with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        new_names = starting_letter.read().replace("[name]", name)

    # Save the letters in the folder "ReadyToSend".

    with open(f"./Output/ReadyToSend/letter for {name}.txt", mode="w") as new_letter:
        new_letter.write(new_names)
