def emoji(msg):
    word = msg.split(" ")
    emojis = {':)': '😁', ':(': '😞'}
    output = " "
    # for item in word:
    #     if item == ':)':
    #         output += print(f' 😁 ')
    #     elif item == ':(':
    #         output += print(f' 😞 ')
    #     else:
    #         output += print(item)

    for item in word:
        output += emojis.get(item, item) + " "
    return output

msg = input(">")
result = emoji(msg)
print(result)
