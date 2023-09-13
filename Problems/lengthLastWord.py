s = "a "

def lengthOfLastWord(s) :
    splited = s.split(" ")
    print(len(splited))
    for i in range(1, len(splited)+1):
        if len(splited[-i]) > 0 :
            return len(splited[-i])

print(lengthOfLastWord(s))