def inverted_triangle(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print(" ")

# n=3
# inverted_triangle(n)

# n=4
# inverted_triangle(n)

n=5
inverted_triangle(n)
