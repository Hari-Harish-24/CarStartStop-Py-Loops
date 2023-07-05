message = input(">")
words = message.split()
output=""
# print(words)
emoji = {
    "sad":":(",
    "happy":":)",
    "shock":":0",
    "love":"(^)"
}
# output = ""
# for i in words:
#     if i in emoji:
#         print("you are in",i,emoji[i])


for i in words:
    output+=emoji.get(i,i) + " "
print(output)