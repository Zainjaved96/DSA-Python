numbers = [1,3,5,6]
target = 7
counter = 1

def findingIndex(numbers,target):
    counters = range(1,numbers[-1])
    for sequence,num in zip(counters,numbers):
        if sequence == num and sequence == target:
            return sequence

print(findingIndex(numbers,target))

        

result = findingIndex(counter,numbers,target)