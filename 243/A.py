inp_ls = [int(key) for key in input().split()]
sums = sum(inp_ls[1:])
last = inp_ls[0] % sums

signal = ["F", "M", "T"]
for i, v in enumerate(inp_ls[1:]):
    last -= v
    if last < 0:
        print(signal[i])
        exit()
