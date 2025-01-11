PLACEHOLDER = "[name]"

with open("input/Names/invited_names.txt") as file:
    content = file.readlines()
with open("input/Letters/starting_letter.txt") as letter:
    invite = letter.read()

for line in content:
    name = line.strip()
    personalized_invite = invite.replace(PLACEHOLDER, name)
    with open(f"output/readyToSend/letter_for_{name}.txt", "w") as final_letter:
        final_letter.write(personalized_invite)

