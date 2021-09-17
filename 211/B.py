s1 = input()
s2 = input()
s3 = input()
s4 = input()

box = set()
box.add(s1)
box.add(s2)
box.add(s3)
box.add(s4)

if "H" in box and "2B" in box and "3B" in box and "HR" in box:
    print("Yes")
else:
    print("No")
