def Emojis(message):
    mood = message.split(" ")
    for word in mood:
        lizt.append(word)
    print(lizt)
    emoji = {"happy": "😁😁", "sad": "🥺🥺", "anxious": "😰", "scared": "🫢🫢🫢", "sleepy": "😴😴😴"}
    output = ""
    for i in lizt:
        output += emoji.get(i, i) + " "
    return output

print("Enter a words that reflects your mood")
message = input("> ")
lizt = ["I","am","feeling"]
print(Emojis(message))