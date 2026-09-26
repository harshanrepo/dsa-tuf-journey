def inverted_pyramid(n):
    for i in range(n):

        # Space:
        for j in range(i):
            print("-",end=" ")

        #Star
        for j in range(2*n-(2*i+1)):
            print("*",end=" ")

        # Space
        for j in range(i):
            print("-",end=" ")
        print(" ")

n=2
inverted_pyramid(n)