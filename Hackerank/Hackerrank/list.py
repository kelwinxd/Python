N = int(input("Type a amount: "))
alist = []

for i in range(N):
    commands = input("type: ")
    com_list = commands.strip().split()
    if com_list[0] == "insert":
        i, e = map(int, com_list[1:])
        alist.insert(i, e)
    elif com_list[0] == "print":
        print(alist)