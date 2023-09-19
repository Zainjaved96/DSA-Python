# Its basically fibonacci sequence lol
n = 3

def climbStairs(n) :
    if n == 1 :
        return 1 
    second_last = 0
    last = 1
    for i in range(1,n+1):
        new = second_last + last 
        second_last = last 
        last = new
    return new

print(climbStairs(n))