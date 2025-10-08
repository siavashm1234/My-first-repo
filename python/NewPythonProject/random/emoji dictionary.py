message = input(">")
emoji={":)" : "😀",
       ":(" : "😞" }
words = message.split(" ")
output = " "
for word in words:
    output =output + emoji.get(word , word)+ " "
print(output)