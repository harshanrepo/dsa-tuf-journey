def pyramid_triangle(n):
    for i in range(n):

        # Space
        for j in range(n-i-1):
            print("-",end=" ")

        # Star
        for j in range(2*i+1):
            print("*",end=" ")

        # Space
        for j in range(n-i-1):
            print("-",end=" ")
        print(" ")

# n=4
# pyramid_triangle(n) 
    
n=2
pyramid_triangle(n)