def emoji_convertor(message):
    emojis = {
        ":)": "🙂",
        ":(": "😥"
    }
    output=""
    message_list = message.split(" ")
    for word in message_list:
        output+= emojis.get(word , word) + " "
    return output

message=input(">")
print(emoji_convertor(message))