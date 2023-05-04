n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("%c"%(i+64),end=" ")
    print(end="
")