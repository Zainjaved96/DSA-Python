a = '1010'
b = '1011'

def addBinary(a,b):
    carry = '0'
    result = ''
    string_not_equal =  True
    while string_not_equal:
        if len(a) > len(b):
            b = '0' + b
        elif len(a) < len(b) :
            a = '0' + a
        if len(a) == len(b):
            string_not_equal = False
            
    for i in reversed(range(0, len(a))):
        sum_of_binary = int(a[i])+ int(b[i]) + int(carry)
        if  sum_of_binary == 0:
            result = '0' + result
            cary = '0'
        elif sum_of_binary == 1:
           result = '1' + result
           carry = '0'
        elif sum_of_binary == 2:
            result = '0' + result
            carry = '1'
        elif sum_of_binary == 3:
            result = '1' + result
            carry = '1'
    
    # Last carry (if theres any)
    if carry == '1':
        result = carry + result

    return result


print(addBinary(a,b))