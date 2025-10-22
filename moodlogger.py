import datetime 
from colorama import init, Fore, Style
init(autoreset=True)
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
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: I am feeling {mood}\n")


color_map={
    "happy":Fore.YELLOW,
    "sad":Fore.BLUE,
    "angry":Fore.RED,
    "excited":Fore.MAGENTA,
    "anxious":Fore.CYAN,
    "neutral":Fore.WHITE,
    "bored":Fore.LIGHTBLACK_EX,
    "tired":Fore.LIGHTBLUE_EX,
    "confused":Fore.LIGHTYELLOW_EX,
    "overwhelmed":Fore.LIGHTRED_EX,
    "content":Fore.LIGHTGREEN_EX,
    "frustrated":Fore.LIGHTMAGENTA_EX,
    "relaxed":Fore.LIGHTCYAN_EX,
    "grateful":Fore.LIGHTGREEN_EX
    
}
with open("mood_log.txt", "r") as file:
    content=file.read()
    print("Your mood log:")
    for line in content.splitlines():
        mood_text=line.lower()
        color=Fore.WHITE
        for key in color_map:
            if key in mood_text:
                color=color_map[key]
                break
        print(color + line.strip())

