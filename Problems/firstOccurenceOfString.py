def strStr(self, haystack: str, needle: str) -> int:
    occured = False
    start_index = -1
    n = 0 
    if needle in haystack:
        for h in range(0,len(haystack)):
            if haystack[h] == needle[0]:
                start_index = h
                counter = h
                if len(needle) > 1:
                    for n in range(1,len(needle)):
                        counter += 1
                        if haystack[counter] == needle[n]:
                            occured = True
                            
                        else:
                            occured = False
                            break
                else:
                    occured = True
            if occured == True:
                break 
    return start_index