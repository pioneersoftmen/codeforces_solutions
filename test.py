def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = string[i]
        str = string[i:i+k]
        for j in range(1, k):
            if str[j] == str[j - 1]:
                continue
            else:
                s += str[j]
        print(s)

s = 'AABCAAADA'
merge_the_tools(s, 3)