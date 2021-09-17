n = int(input())
t = input()

S=""
for i in range(n):
    S += "110"

count=0
for i in range(len(S)-n+1):
    #print(t[:3])
    if str(S[i:i+3])==t[:3]:
        count += 1

#print(count)
print(10**10-(n-count))
