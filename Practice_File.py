def pyramid(n):
    for i in range (1,n+1):
        print(" "*(n-i)+"jumbu"*(2*i-1))

n=int(input())
pyramid(n)
    