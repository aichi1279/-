s = input()
if "R" not in s:
    print(0)
    exit()

list = list(s)

if list[0]==list[1]==list[2]=="R":
    print(3)
elif list[0]==list[1]=="R" or list[1]==list[2]=="R":
    print(2)
else:
    print(1)
