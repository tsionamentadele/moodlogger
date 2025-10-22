moods = []

while True:
    mood=input("How are you feeling today? (Type 'exit' to quit) ")
    if mood.lower() == 'exit':
        break
    moods.append(mood)

    more=input("Would you like to log another mood? (yes/no) ")
    if more.lower() != 'yes':
        break

