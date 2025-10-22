import datetime 
moods = []

while True:
    mood=input("How are you feeling today? (Type 'exit' to quit) ")
    if mood.lower() == 'exit':
        break
    moods.append(mood)

    more=input("Would you like to log another mood? (yes/no) ")
    if more.lower() != 'yes':
        break

with open("mood_log.txt", "a") as file:
    for mood in moods:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: I am feeling {mood}\n")

with open("mood_log.txt", "r") as file:
    content=file.read()
    print("Your mood log:")
    for line in content.splitlines():
        print(f"- {line}")