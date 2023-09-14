digits = [1,2,4]

def plusOne(digits):
    num = ''
    result = []
    for digit in digits:
        num += str(digit)
        print(num)
    incremented = str(int(num) + 1)
    for i in incremented :
        result.append(int(i))
    print( result)
plusOne(digits)