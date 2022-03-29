"""After some commands, let's find our robot's last position"""


command_list = ["right 20", "right 30", "left 50", "up 10", "down 20"]
x = 0
y = 0

for i in range(len(command_list)):
    if command_list[i].startswith("r"): x = x + int(command_list[i].split()[1])
    elif command_list[i].startswith("l"): x = x - int(command_list[i].split()[1])
    elif command_list[i].startswith("u"): y = y + int(command_list[i].split()[1])
    elif command_list[i].startswith("d"): y = y - int(command_list[i].split()[1])

[x,y]
