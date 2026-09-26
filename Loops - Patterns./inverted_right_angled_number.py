def inverted_num(n):
    for i in range(n+1,1,-1):
        for j in range(1,i):
            print(j,end=" ")
        print(" ")

# n=4
# inverted_num(n)

n=2
inverted_num(n)